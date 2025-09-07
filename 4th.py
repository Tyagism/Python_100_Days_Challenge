import os
# this is used to list all files and directories in a specified path.
dir_path = 'c:/'
# this is used to list all files specified path.
content = os.listdir(dir_path)
for item in content:
    print(item)