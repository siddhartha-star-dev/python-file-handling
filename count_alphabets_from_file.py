# Program to get number of alphabets from file
# Created by: Siddhartha
# Created on: 1st April 2020


# function to get the number of alphapets from the file
def get_number_of_alphabets(file):
    # initialize the count as 0
    number_of_alphabets = 0
    # using the read function to get the whole file as a string
    whole_file_as_string = file.read()
    # strip the string of escape sequences
    whole_file_as_string = whole_file_as_string.strip()
    for character in whole_file_as_string:
        # check if the character is an alphabet
        if character.isalpha():
            # append the count variable
            number_of_alphabets += 1
    return number_of_alphabets


# driver function to open the file and process it
def main(fileName, mode):
    with open(fileName, mode) as file:
        number_of_alphabets = get_number_of_alphabets(file)
    return number_of_alphabets


if __name__ == "__main__":
    fileName = 'files/notes.txt'
    mode = 'r'
    number_of_alphabets = main(fileName, mode)
    print("Number of alphabets in the file: {}".format(number_of_alphabets))
