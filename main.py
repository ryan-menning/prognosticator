import pandas as pd
import os


def list_files(files):
    """Accepts a list and returns a dictionary of each item in list with a numbered index (key) starting at 1"""

    dir_list = {}
    file_count = 0
    for file in files:
        file_count +=1
        dir_list[file_count] = file  # assign a number to each item in the list starting with 1 
    return dir_list  # returns dictionary of files in the directory

dirs = sorted(os.listdir('data'))
dir_list = list_files(dirs)  # dict of files in directory

for num, file_name in dir_list.items():
    print(num, ":", file_name)

user_choice = input('Enter the number next to the file to open. (select 0 to exit): ')



    # path = 'data\\'
    # hte = pd.read_csv(path + dir)  # assuming file type will be csv 
    # print(hte.head())
    # print(dir)