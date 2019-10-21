#! /usr/bin/env python3

import pandas as pd
import re
import os


def filepicker():
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()

    file_path = filedialog.askopenfilename()
    return file_path


def read_register():
    print("Please select a downloaded register file")
    filename = filepicker()
    if ".csv" not in filename:
        print("You must select a .csv file, exported from Google forms")
    register = pd.read_csv(filename)
    return register


def get_names(register):
    names = []
    for i in range(len(register) - 1):  # len() -> no of columns
        first_name = str(register.iloc[i][2]).capitalize()
        last_name = str(register.iloc[i][1]).upper()
        name = last_name + ' ' + first_name
        names.append(name)
    names = list(set(names))
    return names


def strip_duds(names):
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
    register = read_register()
    names = get_names(register)
    names = strip_duds(names)
    make_directories(names)
    print(names)


if __name__ == '__main__':
    main()
