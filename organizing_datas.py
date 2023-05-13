import csv
import numpy as np

# to do:
# horizontal values to vertical ?

file_name_no_csv = "test_file"

def get_np_id_from_file(file_name):
    id_list = []

    with open(str(file_name)+'.csv',encoding="utf8") as csv_file: 
        data = csv.reader(csv_file)

        for id in list(data)[0:1]:
            id_list.append(id)
    
    np_id = np.array(id_list)

    return np_id

def get_np_name_from_file(file_name):

    name_list = []

    with open(str(file_name)+'.csv',encoding="utf8") as csv_file: 
        data = csv.reader(csv_file)

        for name in list(data)[1:2]:
            name_list.append(name)

    np_name = np.array(name_list)

    return np_name

def get_np_gmail_from_file(file_name):

    gmail_list = []

    with open(str(file_name)+'.csv',encoding="utf8") as csv_file: 
            data = csv.reader(csv_file)

            for gmail in list(data)[2:3]:
                gmail_list.append(gmail)

    np_gmail = np.array(gmail_list)
    
    return np_gmail

def get_np_number1_from_file(file_name):

    number1_list = []

    with open(str(file_name)+'.csv',encoding="utf8") as csv_file: 
            data = csv.reader(csv_file)

            for number1 in list(data)[3:4]:
                number1_list.append(number1)

    np_number1 = np.array(number1_list)

    return np_number1

def get_np_number2_from_file(file_name):
    
    number2_list = []

    with open(str(file_name)+'.csv',encoding="utf8") as csv_file: 
            data = csv.reader(csv_file)

            for number2 in list(data)[4:]:
                number2_list.append(number2)
    
    np_number2 = np.array(number2_list)

    return np_number2

def convert_np_all_array_to_list(file_name):

    id_list = [] 
    name_list = [] 
    gmail_list = []
    number1_list = [] 
    number2_list = [] 

    id_list = get_np_id_from_file(file_name)
    name_list = get_np_name_from_file(file_name)
    gmail_list = get_np_gmail_from_file(file_name)
    number1_list = get_np_number1_from_file(file_name)
    number2_list = get_np_number2_from_file(file_name)

    new_list = np.dstack((id_list, name_list,gmail_list,number1_list,number2_list))
    
    return new_list

all_data = convert_np_all_array_to_list(file_name_no_csv)

print(all_data.size)