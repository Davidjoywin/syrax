import os
# import threading
import threading


files = []
def scan(path):
    for file_dir in os.listdir(path):
        new_path = os.path.join(path, file_dir)
        if os.path.isfile(new_path):
            file = file_dir
            files.append(os.path.join(path, file))

        elif os.path.isdir(new_path):
            scan(new_path)
            
