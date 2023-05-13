import csv
import numpy as np

# to do:
# horizontal values to vertical ?

file_name_no_csv = "22_s1_les"
new_file_name_yes_csv = str(file_name_no_csv + "_new.csv")

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

def reshaping_3d_to_2d_array(file_name):
    
    all_data = convert_np_all_array_to_list(file_name)

    data_shape = all_data.shape

    sum_shape = sum(data_shape)
    # print(sum_shape)

    row_data = (sum_shape - 6)
    # print(row_data)

    column_data = (sum_shape - row_data - 1)
    # print(column_data)

    reshaped_data = np.reshape(all_data,(row_data,column_data))

    return reshaped_data
    # print(reshaped_data.shape)

def making_new_csv(file_name_old, file_name_new):
    data_to_write = reshaping_3d_to_2d_array(file_name_old)
    
    with open(str(file_name_new), 'w',encoding="utf-8", newline='') as file:
        writer = csv.writer(file)

        writer.writerows(data_to_write)

    print("done writing")

for i in range(1,7):
    file_name_no_csv = "22_s2_les" + str(i)
    new_file_name_yes_csv = str(file_name_no_csv + "_new.csv")
    
    making_new_csv(
        file_name_old=file_name_no_csv,
        file_name_new=new_file_name_yes_csv)