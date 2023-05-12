import csv
import numpy as np

# 22_s1_les.csv
with open('22_s2_les1.csv', newline='', encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)

# print(data)
array1 = np.array(data)
print(array1.dtype) # shape (row, column)

# goal:
# horizontal values to vertical