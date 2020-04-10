# Program to check if file exist and open to read if exist
# Created by: Siddhartha
# Created on: 1st April 2020


if __name__ == "__main__":
    # Input file name
    fileName = input('Enter the path of file: ')
    # Try opening the file
    try:
        file = open(fileName, 'r')
        print("File exists")
    # Catch exception
    except FileNotFoundError:
        print("{} does not exist".format(fileName))
