# Program to display file pointer after reading two lines
# Created by: Siddhartha
# Created on: 1st April 2020


fileName = "files/story.txt"
# open file in read mode
Fn = open(fileName, 'r')

# read two lines one by one
for iter in range(2):
    Fn.readline()


# print the position of pointer
print("Position of pointer {}".format(Fn.tell()))
Fn.close()
