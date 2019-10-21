#! /usr/bin/env python3

"""
This may be a one-off program, depending on changes made to registers.
It reads a SOAS Google Docs register (2019-20) into a pandas dataframe
and creates folders necessary for all academic English student work.

    Student work/
      |
      |___ SURNAME Firstname/
      |    |
      |    |__Term 1/
      |    |
      |    |__Term 2/
      |    |
      |    |__Term 3/
      |
      |____NEXT Student/
      |    |
      |    |__Term 1/
      |    |
      |    |__Term 2/
      |    |
      |    |__Term 3/
"""
import pandas as pd
import re
import os


def filepicker():
    """
    Opens a graphical file selection window, and returns
    the path of the selected file.
    """
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    return file_path


def read_register():
    """
    Opens a csv file (given the filepath, and returns a pandas
    dataframe.
    """
    print("Please select a downloaded register file")
    filename = filepicker()
    if ".csv" not in filename:
        print("You must select a .csv file, exported from Google forms")
    register = pd.read_csv(filename)
    return register


def extract_names(register):
    """
    Extracts the names from the relevant columns of the dataframe.
    This is not a robust function, and will break if the registers
    change the order of the columns.
    """
    names = []
    for i in range(len(register) - 1):  # len() -> no of columns
        first_name = str(register.iloc[i][2]).capitalize()
        last_name = str(register.iloc[i][1]).upper()
        name = last_name + ' ' + first_name
        names.append(name)
    names = list(set(names))
    return names


def clean_names_list(names):
    """
    Takes out NaN entries and 'Surname' & 'firstname' headings.
    This is not a robust function, and will break if the registers
    change their column headings.
    """
    pure_names = []
    nan = re.compile('nan', re.IGNORECASE)
    title = re.compile('surname', re.IGNORECASE)
    for name in names:
        if nan.search(name):
            continue
        elif title.search(name):
            continue
        else:
            pure_names.append(name)
    return pure_names


def make_directories(names):
    """
    Given a list of names, this function creates a
    new directory for each name.
    Within each new directory, sub-directories are
    created: 'Term 1', 'Term 2', 'Term 3'
    """
    os.mkdir('Student_Folders')
    os.chdir('Student_Folders')
    for name in names:
        os.mkdir(name)
        os.chdir(name)
        sub_dirs = ['Term 1', 'Term 2', 'Term 3']
        for drcty in sub_dirs:
            os.mkdir(drcty)
        os.chdir('..')


def main():
    """
    Asks user to select list of names (register).
    and makes a directory for each name.
    """
    register = read_register()
    names = extract_names(register)
    names = clean_names_list(names)
    make_directories(names)
    print(names)


if __name__ == '__main__':
    main()
