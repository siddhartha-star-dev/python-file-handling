# Program to check if a file exist to give an error message if exist
# and to create if not
# Created by: Siddhartha
# Created on: 1st April 2020

import os.path

fileName = input('Enter the path of file: ')
if os.path.exists(fileName):
    print("File exist")
else:
    file = open(fileName, 'w')
    file.close()
