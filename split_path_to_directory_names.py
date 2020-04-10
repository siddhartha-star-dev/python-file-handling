# Program to split path to directory names
# Created by: Siddhartha
# Created on: 1st April 2020


# function to split and return a list of directories
def split_path_to_directories(path):
    list_of_directories = []
    # split at /
    list_splitted = path.split('/')
    for item in list_splitted:
        # check if the item is a filename
        # if it is then it will contain a .
        if '.' not in item:
            # append to the directories' list
            list_of_directories.append(item)
    return list_of_directories


# driver function
def main(path):
    list_of_directories = split_path_to_directories(path)
    for dir_name in list_of_directories:
        print(dir_name)


if __name__ == "__main__":
    path = input("Enter the path: ")
    main(path)
