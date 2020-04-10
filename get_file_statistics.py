# Program to count number of upper case and lower case
# Created by: Siddhartha
# Created on: 1st April 2020


# function to get number of lines
def get_lines(all_lines):
    return len(all_lines)


# function to get the number of empty lines
def get_number_of_empty_lines(all_lines):
    number_of_empty_lines = 0
    for line in all_lines:
        if line == '\n':
            number_of_empty_lines += 1
    return number_of_empty_lines


# function to get average characters per line
def get_average_characters(all_lines):
    num_characters = 0
    num_lines = len(all_lines)
    for line in all_lines:
        for character in line:
            num_characters += 1
    average_characters = num_characters/num_lines
    return average_characters


# function to get average characters per non empty line
def get_average_characters_non_empty_lines(all_lines):
    list_without_empty_lines = []
    for line in all_lines:
        if line != '\n':
            list_without_empty_lines.append(line)
    average_characters_non_empty_lines = get_average_characters(
        list_without_empty_lines
    )
    return (average_characters_non_empty_lines)


def main(fileName, mode):
    with open(fileName, mode) as file:
        all_lines = file.readlines()
        total_lines = get_lines(all_lines)
        number_of_empty_lines = get_number_of_empty_lines(all_lines)
        average_characters = get_average_characters(all_lines)
        average_characters_nel = get_average_characters_non_empty_lines(
            all_lines
        )
        print(
            """
                Total number of lines: {}
                Number of empty lines: {}
                Average characters per line: {}
                Average characters per non empty line: {}
            """.format(
                total_lines,
                number_of_empty_lines,
                average_characters,
                average_characters_nel
            )
        )


if __name__ == "__main__":
    fileName = input("Enter the file path: ")
    mode = 'r'
    main(fileName, mode)
