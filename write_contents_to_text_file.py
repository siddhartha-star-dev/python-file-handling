# Program to write lines in file
# Created by: Siddhartha
# Created on: 1st April 2020

import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s:  %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def enterLineInFile(file, line):
    file.write(line)
    file.write('\n')
    return file


def menu():
    choice = input('Do you want to enter another line[y/n]: ')
    return choice


if __name__ == "__main__":
    logger.info("Opening files/myFile.txt in write mode")
    with open('files/myFile.txt', 'w') as file:
        line = input("Enter a line : ")
        file = enterLineInFile(file, line)
        logger.info("Written line to file succesfully")
        while True:
            choice = menu()
            if choice == 'y' or choice == 'Y':
                line = input('Enter the line: ')
                file = enterLineInFile(file, line)
                logger.info("Written line to file succesfully")
            else:
                logger.info("Exiting program")
                break
