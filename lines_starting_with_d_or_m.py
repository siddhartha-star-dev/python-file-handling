# Program to get numebr of lines starting with digit
# Created by: Siddhartha
# Created on: 1st April 2020


# function to get all the lines starting with d or m
def get_all_lines_with_d_or_m(file):
    # initialize an empty list
    required_lines = []
    all_lines = file.readlines()
    for line in all_lines:
        # check if the initial character d or m
        if line[0] == 'D' or line[0] == 'M':
            # append the line if it satisfies the condition
            required_lines.append(line)
    return required_lines


# driver function to read file and call the above function
def main(fileName, mode):
    with open(fileName, mode) as file:
        # call function to get the list of lines
        required_lines = get_all_lines_with_d_or_m(file)
    return required_lines


if __name__ == "__main__":
    fileName = 'files/delhi.txt'
    mode = 'r'
    required_lines = main(fileName, mode)
    # print the output line by line
    for line in required_lines:
        # ensure that the program doesn't print an extra \n
        print(line, end="")
