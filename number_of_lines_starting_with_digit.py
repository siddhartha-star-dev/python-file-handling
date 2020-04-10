# Program to get numebr of lines starting with digit
# Created by: Siddhartha
# Created on: 1st April 2020


# function to get number of lines starting with a digit
def get_number_of_lines_with_digit(file):
    # initialize total count
    no_of_lines_required = 0
    # get a list of all the lines in the file
    all_lines = file.readlines()
    for line in all_lines:
        # checking if the starting character is a digit
        if line[0].isdigit():
            # append number of lines if true
            no_of_lines_required += 1
    return no_of_lines_required


# Driver function to open file and process it
def main(fileName, mode):
    with open(fileName, mode) as file:
        no_of_lines_required = get_number_of_lines_with_digit(file)
    return no_of_lines_required


if __name__ == "__main__":
    fileName = input('Enter the file path: ')
    mode = 'r'
    number_of_lines = main(fileName, mode)
    print('number of lines starting with digit: {}'.format(
        number_of_lines
    )
    )
