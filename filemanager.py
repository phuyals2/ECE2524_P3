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

        elif user_input == "4":
            print("******-- Rename files --******")
           
        elif user_input == "5":
            print("******-- Delete files --******")
            
        elif user_input == "6":
            print("Exiting...Thank You!!")
            sys.exit(1)

        else:
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
            print("!!          Please select a valid option.         !!")
            print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")


main()
