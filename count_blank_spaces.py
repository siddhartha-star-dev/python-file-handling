# Program to get numebr of occurrence of blank spaces
# Created by: Siddhartha
# Created on: 1st April 2020


# function to count occurance of an alphabet from a file
def count_blank_spaces(file):
    # initialize occurrences as 0
    occurrences = 0
    # using the read function to get the whole file as a string
    whole_file_as_string = file.read()
    # strip string of escape sequences
    whole_file_as_string = whole_file_as_string.strip()
    for character in whole_file_as_string:
        # match the character with blank character
        if character == ' ':
            occurrences += 1
    return occurrences


# driver function to process file and return output
def main(fileName, mode):
    with open(fileName, mode) as file:
        occurrences = count_blank_spaces(file)
    return occurrences


if __name__ == "__main__":
    fileName = 'files/story.txt'
    mode = 'r'
    occurrences = main(fileName, mode)
    print("The blank character occurs {} times".format(occurrences))
