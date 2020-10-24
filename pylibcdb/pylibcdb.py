import wrapper

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