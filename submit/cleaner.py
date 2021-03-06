"""
S20 11-411 NLP Assignment 1 Part 1
Name-Censoring Cleaner Class
Ze Xuan Ong - 25 Jul 19

Cleaner class implements a method clean that, given a list of
censored full names, censored last names, and an input string,
removes the censored full names and last names from the input
and replaces it with a 'politically correct' name.

USAGE: python cleaner.py BANNED_NAMES_FILE INPUT_FILE
BANNED_NAMES_FILE - .txt file containing a list of banned names
INPUT_FILE - .txt file containing the original article

No input validation is performed

Provides an executable script for running implemented class
on a specific file

"""
import re
import sys


class BaseCleaner():
    """
    Abstract class for the text censoring object
    """

    def __init__(self, replacement_full_name, replacement_last_name):
        """
        Initializes Cleaner object
        :param replacement_full_name: full name to replace with
        :param replacement_last_name: last name to replace with
        """
        self.replacement_full_name = replacement_full_name
        self.replacement_first_name = replacement_full_name.split()[0]
        self.replacement_last_name = replacement_last_name

    def clean(self, full_names, last_names, input_text):
        """
        Abstract method, called to censor (replace) text

        :param full_names: a list of full names to replace
        :param last_names: a list of last names to replace
        :param input_text: text string to process
        :return: processed text string
        """
        pass

class Cleaner(BaseCleaner):
    """
    Student submission for text censoring object
    """

    def clean(self, full_names, last_names, input_text):
        """
        Method called to clean input text of censored full names and last names.
        Can assume that list of last names is the set of unique last names derived
        from the list of full names i.e. last_names = list(set([s.split()[-1] for s in full_names]))

        :param full_names: list of censored full names to be replaced
        :param last_names: list of censored last names to be replaced
        :param input_text: input text to process
        :return: output text with censored full names and last names removed
        """
        firstName,lastNamee = self.replacement_full_name.split(" ")
        for fullName in full_names:
            first, last = re.split('[\s]+',fullName)
            #whitespace = ''.join(re.findall('\s+',fullName))
            #input_text = re.sub(r"(?<!-)"+"\\b"+ first + "\s+" + last +"\\b"+r"(?!-)",firstName+whitespace+lastNamee,input_text)
            pattern = r"(?<!-)"+"\\b"+ first + "\s+" + last +"\\b"+r"(?!-)"
            groups = re.findall(pattern,input_text)
            for g in groups:
                whitespace = ''.join(re.findall('\s+',g))
                input_text = re.sub(g,firstName+whitespace+lastNamee,input_text)
        for lastName in last_names:
            input_text = re.sub(r"(?<!-)"+"\\b"+lastName+"\\b"+r"(?!-)",self.replacement_last_name,input_text)

        return input_text
# Main executable script provided for your convenience
# Not executed on autograder, so do what you want
if __name__ == "__main__":

    # Ensure exactly two arguments
    if len(sys.argv) != 3:
        print("Usage: python cleaner.py BANNED_NAMES_FILE INPUT_FILE")
        sys.exit(1)

    BANNED_NAMES_FILE = sys.argv[1]
    INPUT_FILE = sys.argv[2]

    # Check input file type
    if not (BANNED_NAMES_FILE.endswith(".txt") and INPUT_FILE.endswith(".txt")):
        print("Error: BANNED_NAMES_FILE and INPUT_FILE must be .txt files")
        sys.exit(1)

    # Initialize new Cleaner
    cleaner = Cleaner("John Smith", "Smith")

    # Read banned names
    banned_full_names = set()
    with open(BANNED_NAMES_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if line:
                banned_full_names.add(line)
    banned_full_names = list(banned_full_names)
    banned_last_names = list(set([n.split()[-1] for n in banned_full_names]))

    # Read input
    input_contents = ""
    with open(INPUT_FILE, "r") as f:
        input_contents = f.read()
    if not input_contents:
        print("Error: Input file is empty!")
        sys.exit(1)

    # Process and print output
    print(cleaner.clean(banned_full_names, banned_last_names, input_contents))





