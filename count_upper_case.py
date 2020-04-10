# Program to get numebr of lines starting with an upper case character
# Created by: Siddhartha
# Created on: 1st April 2020


# function to count number of lines starting with upper case
def countUpperCase(file):
    # initialize number of lines as 0
    number_of_required_lines = 0
    all_lines = file.readlines()
    for line in all_lines:
        # check if the starting character is upper case
        if line[0].isupper():
            # append to the number of lines variable
            number_of_required_lines += 1
    return number_of_required_lines


# driver function to open file and process it
def main(fileName, mode):
    with open(fileName, mode) as file:
        number_of_required_lines = countUpperCase(file)
    return number_of_required_lines


if __name__ == "__main__":
    fileName = 'files/help.doc'
    mode = "r"
    number_of_lines_with_upper_case = main(
        fileName,
        mode
    )
    print("Number of lines sarting with upper case are: {}".format(
        number_of_lines_with_upper_case
    ))
