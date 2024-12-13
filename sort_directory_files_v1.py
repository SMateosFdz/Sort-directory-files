import os, shutil

#get the current directory and the files inside it
directory = os.getcwd() 
files = os.listdir(directory)

for file in files:
    
    if file != "sort_directory_files.py":
        name, extension = os.path.splitext(file)

        if extension:
            new_directory = os.path.join(directory, extension[1:]) # create new directories with extension names

            if not os.path.exists(new_directory):
                os.makedirs(new_directory)

            shutil.move(os.path.join(directory, file), os.path.join(new_directory, file)) # move the files