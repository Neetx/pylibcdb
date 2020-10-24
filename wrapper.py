import subprocess

def find(address, working_dir):
    completed_process = subprocess.run([working_dir + "/find", "__libc_start_main", address], capture_output=True)
    #proc = subprocess.Popen([working_dir + "/find", "__libc_start_main", address], stdout=subprocess.PIPE, shell=True)
    #(out, err) = proc.communicate()
    libc_list = completed_process.stdout.decode("utf-8").split("\n") #get decoded output into list
    #print(libc_list)
    #print(completed_process.stderr)
    libc_first = libc_list[0]   #get first element
    libc_name = libc_first.split('(', 1)[1].split(')')[0] #get the string within ()
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
    #print (path)
    completed_process = subprocess.run("ls " + path + "/libc-*.so", shell=True, cwd =path + "/" ,capture_output=True) #passing string instead of list works
    #print(completed_process.stdout)
    #print(completed_process.stderr)
    #print(completed_process.args)
    return completed_process.stdout.decode("utf-8")[:-1]