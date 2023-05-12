import csv

# 22_s1_les.csv
with open('22_s2_les1.csv', newline='', encoding="utf8") as f:
    reader = csv.reader(f)
    data = list(reader)

print(data)