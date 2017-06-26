import os, time


class Directory:
    def __init__(self, dir_path, dir_size):
        self.dir_path = dir_path
        self.dir_size = dir_size

def b_to_gb(in_bytes):
    in_gb = in_bytes / (1024*1024*1024)
    return in_gb

def get_big_dir(size_check=1073741824, directory="c:"):
    os.chdir(directory)
    dir_list = []

    def get_dir_sizes(next_path ='.'):
        current_path = os.path.join(os.getcwd(),next_path)
        curr_dir = Directory(dir_path=current_path, dir_size=0)
        try:
            os.chdir(next_path)
        except (PermissionError, FileNotFoundError): #hack move to handle paths os doesn't like
            return 0
        try:
            dir_names = [d for d in os.listdir('.') if os.path.isdir(d)]
        except PermissionError:
            dir_names = []
        try:
            file_names = [f for f in os.listdir('.') if os.path.isfile(f)]
        except PermissionError:
            file_names = []
        for dir in dir_names:
            curr_dir.dir_size += get_dir_sizes(dir)
        for file in file_names:
            file_path = os.path.join(current_path, file)
            curr_dir.dir_size += os.path.getsize(file_path)
        if (curr_dir.dir_size > size_check):
            dir_list.append(curr_dir)
        os.chdir('..')
        return curr_dir.dir_size
    total_size = get_dir_sizes()
    return dir_list, total_size