# Program to accept a file from user and display all the lines which
# contain python character '#'
# Created by: Siddhartha
# Created on: 1st April 2020


def get_lines_with_hash(file):
    linesWithHash = []
    for line in file.readlines():
        if '#' in line:
            linesWithHash.append(line)
    return linesWithHash


def main(fileName, mode):
    with open(fileName, mode) as file:
        linesWithHash = get_lines_with_hash(file)
    return linesWithHash


if __name__ == "__main__":
    fileName = input('Enter the file path: ')
    mode = 'r'
    linesWithHashes = main(fileName, mode)
    print("The lines containing hash are : \n")
    print(*linesWithHashes, sep="\n")
