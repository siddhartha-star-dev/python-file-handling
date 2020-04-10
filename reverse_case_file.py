# Program that reads a text file and
# create a text file that reverse case of every letter
# Created by: Siddhartha
# Created on: 5th April 2020


# function for changing the case of character of line
def reverse_case(line):
    new_line = ''
# loop to check case of letters in line and change it
    for letter in line:
        if letter.isupper():
            new_line += letter.lower()
        elif letter.islower():
            new_line += letter.upper()
    return new_line


if __name__ == "__main__":
    file = input('Enter the path of file: ')
    file1 = input('Enter the path of file which has case reversed: ')
    with open(file, 'r') as file:
        with open(file1, 'w+') as file1:
            for line in file.readlines():
                file1.write(reverse_case(line))
                file1.write('\n')
    print('{} is made succesfully.'.format(file1))
