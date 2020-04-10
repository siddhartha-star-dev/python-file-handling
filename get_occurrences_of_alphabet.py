# Program to get numebr of occurrence of an alphabet
# Created by: Siddhartha
# Created on: 1st April 2020


# function to count occurance of an alphabet from a file
def count_an_alphabet(file, alphabet):
    # initialize occurrences as 0
    occurrences = 0
    # using the read function to get the whole file as a string
    whole_file_as_string = file.read()
    # strip string of escape sequences
    whole_file_as_string = whole_file_as_string.strip()
    for character in whole_file_as_string:
        # match the character with the parameter alphabet
        if character == alphabet:
            occurrences += 1
    return occurrences


# driver function to process file and return output
def main(fileName, mode, alphabet):
    with open(fileName, mode) as file:
        occurrences = count_an_alphabet(file, alphabet)
    return occurrences


if __name__ == "__main__":
    fileName = input("Enter file name: ")
    mode = 'r'
    alphabet = input("Enter the alphabet you want to search : ")
    occurrences = main(fileName, mode, alphabet)
    print("The alphabet {} occurs {} times".format(alphabet, occurrences))
