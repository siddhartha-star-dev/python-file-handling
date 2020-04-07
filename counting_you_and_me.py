# Program to count no. of you and me in a text file
# Created by: Siddhartha
# Created on: 1st April 2020


def Me(file):
    count = 0
    for line in file.readlines():
        line = line.lower().strip().split(" ")
        count += line.count("me")
    file.seek(0)
    return count


def You(file):
    count = 0
    for line in file.readlines():
        line = line.lower().strip().split(" ")
        count += line.count("you")
    file.seek(0)
    return count


def main(fileName, mode):
    with open(fileName, mode) as file:
        no_of_you = You(file)
        no_of_me = Me(file)
    yield no_of_you
    yield no_of_me


if __name__ == "__main__":
    fileName = input('Enter the file path: ')
    mode = 'r'
    list_output = list(main(fileName, mode))
    print('number of you: {} and me: {}'.format(
        list_output[0],
        list_output[1]
        )
    )
