import csv
import numpy as np

# 22_s1_les.csv
# with open('22_s2_les1.csv', newline='', encoding="utf8") as f:
#     reader = csv.reader(f)
#     data = list(reader)


# to do:
# horizontal values to vertical ?

id_line = []
name_line = []
gmail_line = []
number1_line = []
number2_line = []

with open('test_file.csv',encoding="utf8") as csv_file: 
    data = csv.reader(csv_file)

    # taking id line
    for id in list(data)[0:1]:
        id_line.append(id)

with open('test_file.csv',encoding="utf8") as csv_file: 
    data = csv.reader(csv_file)

    # taking name line
    for name in list(data)[1:2]:
        name_line.append(name)

with open('test_file.csv',encoding="utf8") as csv_file: 
    data = csv.reader(csv_file)

    # taking name line
    for gmail in list(data)[2:3]:
        gmail_line.append(gmail)

with open('test_file.csv',encoding="utf8") as csv_file: 
    data = csv.reader(csv_file)

    # taking name line
    for number1 in list(data)[3:4]:
        number1_line.append(number1)

with open('test_file.csv',encoding="utf8") as csv_file: 
    data = csv.reader(csv_file)

    # taking name line
    for number2 in list(data)[4:]:
        number2_line.append(number2)

# convert list to np array
np_id_line = np.array(id_line)
np_name_line = np.array(name_line)
np_gmail_line = np.array(gmail_line)
np_number1_line = np.array(number1_line)
np_number2_line = np.array(number2_line)

print("\n id line\n",np_id_line)
print("\n name line\n",np_name_line)

np_new_line = np.dstack((np_id_line, np_name_line,np_gmail_line,np_number1_line,np_number2_line))
print("\n new list\n",np_new_line.shape)

