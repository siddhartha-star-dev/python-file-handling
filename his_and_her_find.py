# Program to count no. of her and his in a text file
# Created by: Siddhartha
# Created on: 1st April 2020


# Function to count his
def His(file):
    count = 0
    for line in file.readlines():
        # removing escape seq. and converting to lower case
        line = line.lower().strip().split(' ')
        # counting number of his
        count += line.count('his')
    file.seek(0)
    return count


# Same as above function but for counting her
def Her(file):
    count = 0
    for line in file.readlines():
        line = line.lower().strip().split(' ')
        count += line.count('her')
    file.seek(0)
    return count


# Driver function to open file and process it
def main(fileName, mode):
    with open(fileName, mode) as file:
        no_of_his = His(file)
        no_of_her = Her(file)
    yield no_of_her
    yield no_of_his


if __name__ == "__main__":
    fileName = input('Enter the file path: ')
    mode = 'r'
    list_output = list(main(fileName, mode))
    print('number of her: {} and his: {}'.format(
        list_output[0],
        list_output[1]
        )
    )
