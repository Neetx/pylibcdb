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

from . import wrapper

class LibcDB:
    working_dir = None
    libc_name = None
    libc_path = None
    def __init__(self, working_dir):
        self.working_dir = working_dir

    def cwd(self, working_dir):
    	self.working_dir = working_dir

    def find_by_address(self, leaked_address):
        self.libc_name = wrapper.find(leaked_address, self.working_dir)
        return self.libc_name

    def download_by_name(self, libc_name):
    	self.libc_path = wrapper.download(libc_name, self.working_dir)
    	return self.libc_path

    def get_working_dir(self):
    	return self.working_dir

    def get_libc_name(self):
    	return self.libc_name

    def get_libc_path(self):
    	return self.libc_path