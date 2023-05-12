import csv
import numpy as np

# 22_s1_les.csv
with open('22_s2_les1.csv', newline='', encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)

# print(data)
array1 = np.array(data)
print(array1.dtype) # shape (row, column)

# to do:
# horizontal values to vertical ?

# r.n my data:
# id - 0,0,0
# name - a,a,a
# gmail - @,@,@
# num1 - 1,1,1
# num2 - 2,2,2

# wanted data:
# id, name, gmail, num1, num2
# 0,a,@,1,2
# 0,a,@,1,2

