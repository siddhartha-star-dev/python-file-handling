# Program to check if file exist and open to read if exist
# Created by: Siddhartha
# Created on: 1st April 2020


if __name__ == "__main__":
    fileName = input('Enter the path of file: ')
    try:
        file = open(fileName, 'r')
        print("File exists")
    except FileNotFoundError:
        print("{} does not exist".format(fileName))
