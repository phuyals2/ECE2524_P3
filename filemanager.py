import sys
import os

# This function prompts for a valid directory path.
# If the entered path is invalid, it will keep prompting the user to input a valid path
def verify_path():
    my_path = input('Enter a directory path:')
    if os.path.isdir(my_path):
        return my_path
    else:
        print("Please enter a valid path!\n ")
        dir_path = verify_path()
        return dir_path


# This function is called when option 1 is selected from the menu.
# It uses the os module to recursively traverse the user provided directory.    
def traverse_directory(my_path):
    print("\n")  
    for root, dirs, files in os.walk(my_path):
        level = root.replace(my_path, '').count(os.sep)
        shift = ' ' * 4 * level
        print(' {}{}: '.format(shift, "Inside --> " + os.path.basename(root)))
        bulleted = ' ' * 6 * (level + 2)
        for i in files:
            print(' {}{}'.format(bulleted, "- " + i))
    print("----------------------------------------------------------\n") 
   

 # This is the function called to rename files. Parameters passed are the directory path, new name, and file extension.
 # This function will check if a file of given extension exists in a directory or not.
          # - If it exists, it will rename the file with the name passed by the user.
          #  - It will also append numbers at the end of the new name starting from 0 ( This will depend on file's postion inside the for loop).
          # - If it does not exist, it will simply return false     
 def rename_files(path, new_name, file_type):
    check = False
    verify = False
    temp_files = os.listdir(path)  # lists the files in the specified path
    files = sorted(temp_files)

    for index, file in enumerate(files):
        if file.endswith(file_type):  # Checking if the filetype exists in the directory
            os.rename(os.path.join(path, file), os.path.join(path, ''.join([new_name, str(index), "." + file_type])))
            check = True
            verify = True
        else:
            check = False
    return verify  

# This is the function called when the user wants to delete a file of certain extension from a folder. 
# The parameters aree directory path and file extenstion.
     # - If a file of certain extension exists, it will simply delete that file.
     # - If it doesn't exist, it will return a boolean value of false. 
def delete_files(path, file_type):
    check = False
    verify = False
    test = os.listdir(path)

    for item in test:
        if item.endswith(file_type):
            os.remove(os.path.join(path, item))
            check = True
            verify = True
        else:
            check = False

    return verify

  # This function will arrange the files a given directory based on the file size and print them out in the console.
  # It will arrange files in ascending order.
 def arrange_by_size(path):
    os.chdir(path)
    # creating a dictionary to hold files
    my_dictionary = {}
    print("Arranging by size: \n")
    for files in os.listdir(path):
        if os.path.isfile(files):
            my_dictionary[files] = os.stat(files).st_size  # this gives size in bytes

    print(f'\tFiles {6 * "  "}\t File Size \n ')

    for file, size in sorted(my_dictionary.items(), key=lambda s: (s[1], s[0])):   # This will sort the files in required order
        print(f"{file:<30} {size / 1000:.03f} KB")  # Formatting the output

    print("------------------------------------------------------------------------\n")   
          
  
  # This function will arrange the files in the given directory by the date/time they were created and display them in the console        
 def arrange_by_time(path):
    my_list = (os.path.join(path, f) for f in os.listdir(path))  # listing the files in the specified path
    my_list = ((os.stat(path), path) for path in my_list)  # listing the files with stat
    my_list = ((stat[ST_CTIME], path) for stat, path in my_list if S_ISREG(stat[ST_MODE]))

    print(f'\tFiles {6 * "  "}\t\t Date/Time created \n ')
    for my_time, path in sorted(my_list):
        print(f"{os.path.basename(path):<40}{time.ctime(my_time)} ")
    print("-----------------------------------------------------------------------\n")
          
 # This function simply prints the welcome screen menu   
def print_menu():
    print("\n")
    print("\t***************************")
    print("\t     !!-- Welcome -- !!    ")
    print("\t***************************")
    print("=================================================\n"
          "\t\tAvailable options: \n"
          "=================================================\n"
          "\t1] - Generate directory tree \n"
          "\t2] - List files by size\n"
          "\t3] - List files by creation date/time\n"
          "\t4] - Rename files \n"
          "\t5] - Delete files\n"
          "\t6] - Exit\n"
          "=================================================\n")

# This is the main function which will call different functions above based on the task selected by the user.
def main():
    print_menu()
    while True:
        print("[press 0 to view menu] ")
        user_input = input("Enter an option number from the menu: ")

        if user_input == "0":
            print(
                "##################################################\n"
                "\t1] - Generate directory tree\n"
                "\t2] - List files by size\n"
                "\t3] - List files by date/time\n"
                "\t4] - Rename files based on extension\n"
                "\t5] - Delete files based on extension\n"
                "\t6] - Exit\n"
                "##################################################\n")

        elif user_input == "1":
            print(" \n")
            print("******-- Walking a directory --*******")
            my_path = verify_path()
            traverse_directory(my_path)
            print("\n")

        elif user_input == "2":
            print(" \n")
            print("******-- Arranging files by size --*****")
            my_path = verify_path()
            arrange_by_size(my_path)

        elif user_input == "3":
            print(" \n")
            print("******-- Arranging files by date/time --*****")
            my_path = verify_path()
            arrange_by_time(my_path)

        elif user_input == "4":
            print("******-- Rename files --******") 
             my_path = verify_path()
            file_type = input("Enter the file(s) extension: ")
            new_name = input("Enter the new name for files: ")
            check = rename_files(my_path, new_name, file_type)

            if check is True:
                print(" All the files of type " + file_type + " have been successfully renamed!!\n")
                print("----------------------------------------------------------\n")
            elif check is False:
                print(" !!The specified file type does not exist in the provided directory!! ")
                print("----------------------------------------------------------\n")
          
           
        elif user_input == "5":
            print("******-- Delete files --******")
            my_path = verify_path()
            file_type = input("Enter the file(s) extension: ")
            check = delete_files(my_path, file_type)
            if check is True:
                print(" All the files of type " + file_type + " have been successfully deleted!!\n")
                print("----------------------------------------------------------\n")
            elif check is False:
                print(" !!The specified file type does not exist in the provided directory!! ")
                print("----------------------------------------------------------\n")

            
        elif user_input == "6":
            print("Exiting...Thank You!!")
            sys.exit(1)

        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!!          Please select a valid option.         !!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


main()
