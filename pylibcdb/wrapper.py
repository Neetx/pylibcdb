"""
Copyright 2020 Neetx

This file is part of pylibcdb.

pylibcdb is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pylibcdb is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with pylibcdb.  If not, see <http://www.gnu.org/licenses/>.
"""

import subprocess

def find(address, working_dir, symbol="__libc_start_main"):
    completed_process = subprocess.run([working_dir + "/find", symbol, address], capture_output=True)
    #proc = subprocess.Popen([working_dir + "/find", "__libc_start_main", address], stdout=subprocess.PIPE, shell=True)
    #(out, err) = proc.communicate()
    libc_list = completed_process.stdout.decode("utf-8").split("\n") #get decoded output into list
    #print(libc_list)
    #print(completed_process.stderr)
    libc_list = libc_list[:-1]
    if len(libc_list) > 1:
        print("Select version:")
        for i, lib in enumerate(libc_list):
            print(str(i+1) + " - " + lib)
        choice = input(">")
        if int(choice) <= len(libc_list) and int(choice) >= 1:
            libc_choice = libc_list[int(choice)-1]
        else:
            print("Invalid choice, exiting...")
            exit(0)
    else:
        libc_choice = libc_list[0]  
    libc_name = libc_choice.split('(', 1)[1].split(')')[0] #get the string within ()
    return libc_name

def download(libc_name, working_dir):
    completed_process = subprocess.run([working_dir + "/download", libc_name], capture_output=True)
    #proc = subprocess.Popen([working_dir + "/download", libc_name], stdout=subprocess.PIPE, shell=True)
    #(out, err) = proc.communicate()
    output_lines = completed_process.stdout.decode("utf-8").split("\n") #get decoded output into list
    second_last_line = output_lines[-2:-1][0]  #get second_last element which contain the path and pop from list
    if len(output_lines)>2: #if it is a new libc
        #print("New libc")
        prefix = "  -> Package saved to "
        path = second_last_line[len(prefix):] #estract the good output
    else: #if we already have this libc
        #print("Known libc")
        prefix = "Getting "
        path = "libs/" + second_last_line[len(prefix):] #estract the good output
    path = working_dir + "/" + path
    #print ("ls " + path + "/libc-*.so")
    completed_process = subprocess.run("ls " + path + "/libc-*.so", shell=True, cwd =path + "/" ,capture_output=True) #passing string instead of list works
    #print(completed_process.stdout)
    #print(completed_process.stderr)
    #print(completed_process.args)
    return completed_process.stdout.decode("utf-8")[:-1]