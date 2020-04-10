# Program to display all contentof file
# and remove all following and trailing white space
# Created by: Siddhartha
# Created on: 11th April 2020


def new_line(line):
    new_line = ''
    for word in line.split():
        line += word + ' '
    return new_line


if __name__ == "__main__":
    fileName = 'files/delhi.txt'
    mode = 'r'
    with open(fileName, mode) as file:
        for line in file.readlines():
            print(new_line(line))
