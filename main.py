import pandas as pd
import os


def list_files(files):
    """Accepts a list and returns a dictionary of each item in list with a numbered index (key) starting at 1"""

    dir_list = {0:'Exit'}
    file_count = 0
    for file in files:
        file_count +=1
        dir_list[file_count] = file  # assign a number to each item in the list starting with 1 
    return dir_list  # returns the dictionary of items in the list

def print_dict(dict_items):
    """Prints the (key : value) pairing in a dictionary"""

    for key, value in dict_items.items():
        print(key, ":", value)

def check_dict(dict_to_check, choice):
    """Checks if the input choice is a key in the provided dictionary
        and returns 'valid' if true, 'invalid' if false"""

    if choice in dict_to_check:
        key_exists = "valid"
    else:
        key_exists = "invalid"

    return key_exists

def error_message(invalid_choice):
    print(f"Your input of '{invalid_choice}' is not a valid choice. Try again!")
    print()

def validate_int(user_input):
    """Checks if user input is an int. If not returns 'is_not_int'"""

    try:
        int(user_choice)
    except ValueError:
        print(f"'{user_choice}' is not an integer.")
        return "is_not_int"

dirs = sorted(os.listdir('data'))
dir_list = list_files(dirs)  # returned dict of files in directory

print_dict(dir_list)
user_choice = input('Enter the number next to the file to open. (0 to exit): ')

int_check = validate_int(user_choice)
if int_check == "is_not_int":
    validate_choice = "invalid"
else:
    validate_choice = check_dict(dir_list, int(user_choice)) # check to see if user input is a key in the dictionary

while validate_choice == "invalid":
    error_message(user_choice)
    print_dict(dir_list)
    user_choice = input('Enter the number next to the file to open. (0 to exit): ')
    int_check = validate_int(user_choice)
    if int_check == "is_not_int":
        validate_choice = "invalid"
    else:
        validate_choice = check_dict(dir_list, int(user_choice)) # check to see if user input is a key in the dictionary

    if user_choice == 0:
        break
    

print(f"{user_choice} is a valid choice")

print(dir_list[int(user_choice)])

if int(user_choice) != 0:
    df_all_specs = pd.read_csv('specifications.csv').set_index('Color')  # read all product specifications into a df
    file_to_open = 'data/' + dir_list[int(user_choice)]
    df = pd.read_csv(file_to_open)
    # prod = dir_list[int(user_choice)].rstrip(".csv")  # assuming all file choices are CSV files
    prod = os.path.splitext(dir_list[int(user_choice)])[0]  # splitting filename from extension 
    df_prod_specs = df_all_specs.iloc[lambda x: x.index == prod]



    print(df.describe())

    print(df.head())
    column_selection = list_files(df.columns)
    print(column_selection)

# while user_choice != 0:






    # path = 'data\\'
    # hte = pd.read_csv(path + dir)  # assuming file type will be csv 
    # print(hte.head())
    # print(dir)