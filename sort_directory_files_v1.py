import os, shutil

#get the current directory and the files inside it
directory = os.getcwd() 
files = os.listdir(directory)


for file in files:
    flag = False #flag used to allow the user to choose if create a directory to a certain extension or not

    if file != os.path.basename(__file__): #avoid to move this python file, but not others
        name, extension = os.path.splitext(file) #split the filename into name and extension
        
        if extension:
            while flag == False:

                print("Do you want to sort the " + extension + " extension? 1 - Yes, 2 - No")
                value = input()

                try:
                    if int(value) == 1:
                        new_directory = os.path.join(directory, extension[1:]) # create new directories with extension names

                        if not os.path.exists(new_directory):
                            os.makedirs(new_directory)

                        shutil.move(os.path.join(directory, file), os.path.join(new_directory, file)) # move the files
                        flag = True

                    elif int(value) == 2:
                        flag = True
                    
                    else:
                        print("Input incorrect, try again")

                except:
                    print("Input incorrect, try again")