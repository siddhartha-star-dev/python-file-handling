# Program to count number of upper case and lower case
# Created by: Siddhartha
# Created on: 1st April 2020


# function to count number of upper case and lower case
def countUpperAndLowerCase(file):
    # initialize number of upper case as 0
    number_of_upper = 0
    # initialize number of lower case as 0
    number_of_lower = 0
    # using read to get whole file as a string
    whole_file_as_string = file.read()
    for character in whole_file_as_string:
        if character.isupper():
            number_of_upper += 1
        if character.islower():
            number_of_lower += 1
    yield number_of_upper
    yield number_of_lower


# driver function to open file and process it
def main(fileName, mode):
    with open(fileName, mode) as file:
        list_of_counts = list(countUpperAndLowerCase(file))
    return list_of_counts


if __name__ == "__main__":
    fileName = 'files/book.txt'
    mode = "r"
    list_of_counts = main(
        fileName,
        mode
    )
    print("Number of upper case: {} Number of lower case: {}".format(
        list_of_counts[0],
        list_of_counts[1]
    ))
