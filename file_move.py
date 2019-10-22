"""
A script that moves files and directories from source to destination 

The script gets 3 inputs:

- txt file path that contains the names of files and directoris to be transferred 
- source directory, supplied as: c:\path
- destination directory, supplied as: c:\path
"""

import shutil
list_of_files = []
txt_file_path = input("Please insert the text file path containing the files to be transferred: ")
src_dir = input("Please enter the source directory to transfer the files from: ")
dst_dir = input("Please enter the destination directory to transfer the files to: ")

# Open text file in read mode
txtfile = open(txt_file_path, "r")
print("Opening file containing list of files to transfer")
# iterate over the lines and append them to a list
for line in txtfile.readlines():
    print("Appending the following file to the list: %s" % line)
    list_of_files.append(line.strip())
print(list_of_files)
txtfile.close()
# iterate over the objects in the list and move them from the source to the destination
for f in list_of_files:
    shutil.move(src_dir + "\\%s" % f, dst_dir + "\\%s" % f)
    print("Moved the following files: %s" % f)
