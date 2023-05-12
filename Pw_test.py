import requests 
from bs4 import BeautifulSoup
import csv

login_url = "https://lms.must.edu.mn/"
check = "2"
login = "" 
password = ""

with requests.session() as s: 
	req = s.get(login_url).text 
	html = BeautifulSoup(req,"html.parser") 
	token = html.find("input", {"name": "__RequestVerificationToken"}). attrs["value"] 
	
payload = { 
	"__RequestVerificationToken": token,
	"type": check,
	"code": login, 
	"password": password
}

res = s.post(login_url, data=payload) 
print(res.url) # print opened url

# opening english department site
students_url = "https://lms.must.edu.mn/Student/Lesson?lcode=S.CE102&tcode=B.ES60&type=students&ltp=c"
r = s.get(students_url) 
soup = BeautifulSoup(r.content, "html.parser")
repos = soup.find_all("div",class_="student-info") 

all_ids = []

# getting all the students
for i in repos:
    id = i.find("p").getText()
    # print(type(id)) str
    all_ids.append(id)


# print(all_ids)
del all_ids[0] # deleting "bagsh"
new_id = []

# removing /tanhimaar/
for id in all_ids:
    splited = id.split(" ")
    splited.remove('/танхимаар/')
    new_id.append(splited)

all_ids.clear()

for i in new_id:
    for j in range(0,1):
        all_ids.append(i[j])

my_id_index = all_ids.index("B221880037")

all_ids.pop(my_id_index)

# print("\n",all_ids)
print("ids done")

all_names = []
all_gmails = []
all_numbers1 = []
all_numbers2 = []

# opening student 
for i in range(0,len(all_ids)):
    one_student_url = "https://lms.must.edu.mn/Student/user?code="+str(all_ids[i])
    # print(one_student_url)
    r = s.get(one_student_url) 
    soup = BeautifulSoup(r.content, "html.parser")
    name = soup.find("p", attrs={"class": "name"}).get_text()
    name = str(name).replace("                    Чатлах", "")
    name = name.replace("\r\n","")
    all_names.append(name.split(" ")[0])
# print("\n",all_names)

print("names done")

for i in range(0,len(all_ids)):
    one_student_url = "https://lms.must.edu.mn/Student/user?code="+str(all_ids[i])
    # print(one_student_url)
    r = s.get(one_student_url) 
    soup = BeautifulSoup(r.content, "html.parser")
    number = soup.find("p", attrs={"class": "number"}).get_text()
    number = number.replace("\r\n","")
    all_gmails.append(number.split(" ")[0])
# print("\n",all_gmails)
print("gmails done")

new_numbers = []
for i in range(0,len(all_ids)):
    one_student_url = "https://lms.must.edu.mn/Student/user?code="+str(all_ids[i])
    # print(one_student_url)
    r = s.get(one_student_url) 
    soup = BeautifulSoup(r.content, "html.parser")
    number1 = soup.find_all("p", attrs={"class": "number"})[1]
    new_numbers.append(number1.contents)

all_numbers1.clear()
for i in new_numbers:
    for j in range(0,1):
        all_numbers1.append(i[j])

# print("\n",all_numbers1)
print("number 1 done")

new_numbers.clear()
for i in range(0,len(all_ids)):
    one_student_url = "https://lms.must.edu.mn/Student/user?code="+str(all_ids[i])
    # print(one_student_url)
    r = s.get(one_student_url) 
    soup = BeautifulSoup(r.content, "html.parser")
    number2 = soup.find_all("p", attrs={"class": "number"})[2]
    new_numbers.append(number2.contents)

all_numbers2.clear()
for i in new_numbers:
    for j in range(0,1):
        all_numbers2.append(i[j])

# print("\n",all_numbers2)
print("number 2 done")

# all_ids = ",".join(all_ids)
# all_names = ",".join(all_names)
# all_gmails = ",".join(all_gmails)
# all_numbers1 = ",".join(all_numbers1)
# all_numbers2 = ",".join(all_numbers2)

with open('eng2.csv', 'w',encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(list(all_ids))
    writer.writerow(all_names)
    writer.writerow(all_gmails)
    writer.writerow(all_numbers1)
    writer.writerow(all_numbers2)
