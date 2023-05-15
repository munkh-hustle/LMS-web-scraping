import requests
from bs4 import BeautifulSoup
import csv
import numpy as np
import pandas as pd

new_list = []
# getting data from all data other files

with open(str("all_students") + '.csv', encoding="utf8") as csv_file:
    data = csv.reader(csv_file)
    for id in list(data)[:]:
        new_list.append(id)

np_new = np.array(new_list)
np_new = np.unique(np_new, axis=0)  # remove duplicates

np_new = np_new[np_new[:, 0].argsort()]  # sort by index 0 (by student id)

# creating csv file
np_id = np_new[:, 0]



# getting img

for i in range(0, len(np_id)):
        img_url = 'https://lms.must.edu.mn/Image?code=' + str(np_id[i])
        # login_url = "https://lms.must.edu.mn/"
        login_url = "https://lms.must.edu.mn/Image?code=" + str(np_id[i])
        check = "2"
        login = ""
        password = ""
        
        with requests.session() as session:
            req = session.get(login_url).text
            html = BeautifulSoup(req, "html.parser")
            # token = html.find("input", {"name": "__RequestVerificationToken"}).attrs["value"]
            payload = {
                # "__RequestVerificationToken": token,
                "type": check,
                "code": login,
                "password": password
            }
        
            res = session.post(login_url, data=payload)
            print(res.url)
        response = requests.get(img_url)
        print(response)
        if response.status_code:
            fp = open('images_by_id/' + str(np_id[i]) + '.png', 'wb')
            fp.write(response.content)
            fp.close()

      # print opened url

def get_all_student_ids_from_lesson(lesson_url,is_print):

    all_id = []

    whole_site = session.get(lesson_url)
    soup = BeautifulSoup(whole_site.content, "html.parser")
    repos = soup.find_all("div",class_="student-info")

    # get all student's ids
    for i in repos:
        id = i.find("p").getText()
        all_id.append(id)
    
    # print(all_id)

    del all_id[0] # deleting "bagsh"
    # del all_id[0]
    # del all_id[0]

    # print(all_id)

    temp_student_idS = []

    # remove /танхимаар/
    for id in all_id:
        splited = id.split(" ")
        splited.remove('/танхимаар/')
        temp_student_idS.append(splited)
    
    all_id.clear() # clearing old data
    
    # convert 2D list to 1D list
    for i in temp_student_idS:
        for j in range(0,1):
            all_id.append(i[j])

    if is_print == True:
        print(all_id)
    
    # delete my id 
    my_id_index = all_id.index("B221880037")
    all_id.pop(my_id_index)

    print("id done")

    return all_id

def get_all_student_names_by_id(all_id,is_print):

    all_name = []

    for i in range(0,len(all_id)):
        one_student_url = "https://lms.must.edu.mn/Student/user?code="+str(all_id[i])
        # print(one_student_url)
        r = session.get(one_student_url) 
        soup = BeautifulSoup(r.content, "html.parser")
        name = soup.find("p", attrs={"class": "name"}).get_text()
        name = str(name).replace("                    Чатлах", "")
        name = name.replace("\r\n","")
        all_name.append(name.split(" ")[0])

    if is_print == True:
        print(all_name)

    print("name done")
    return all_name

def get_all_student_gmails_by_id(all_id, is_print):
    
    all_gmail = []

    for i in range(0,len(all_id)):
        one_student_url = "https://lms.must.edu.mn/Student/user?code="+str(all_id[i])
        # print(one_student_url)
        r = session.get(one_student_url) 
        soup = BeautifulSoup(r.content, "html.parser")
        number = soup.find("p", attrs={"class": "number"}).get_text()
        number = number.replace("\r\n","")
        all_gmail.append(number.split(" ")[0])

    if is_print == True:
        print(all_gmail)

    print("gmail done")
    return all_gmail

def get_all_student_number1_by_id(all_id, is_print):
    
    temp_number = []
    all_number1 = []

    for i in range(0,len(all_id)):
        one_student_url = "https://lms.must.edu.mn/Student/user?code="+str(all_id[i])
        # print(one_student_url)
        r = session.get(one_student_url) 
        soup = BeautifulSoup(r.content, "html.parser")
        number1 = soup.find_all("p", attrs={"class": "number"})[1]
        temp_number.append(number1.contents)

    all_number1.clear()
    for i in temp_number:
        for j in range(0,1):
            all_number1.append(i[j])

    if is_print == True:
        print(all_number1)
    
    print("number1 done")

    return all_number1

def get_all_student_number2_by_id(all_id, is_print):

    temp_number = []
    all_number2 = []

    temp_number.clear()
    for i in range(0,len(all_id)):
        one_student_url = "https://lms.must.edu.mn/Student/user?code="+str(all_id[i])
        # print(one_student_url)
        r = session.get(one_student_url) 
        soup = BeautifulSoup(r.content, "html.parser")
        number2 = soup.find_all("p", attrs={"class": "number"})[2]
        temp_number.append(number2.contents)

    all_number2.clear()
    for i in temp_number:
        for j in range(0,1):
            all_number2.append(i[j])

    if is_print == True:
        print(all_number2)

    print("number2 done")

    return all_number2

def write_student(file_name,all_id,all_name,all_gmail,all_number1,all_number2):
    
    with open(str(file_name), 'w',encoding="utf-8", newline='') as file:
        writer = csv.writer(file)

        writer.writerow(list(all_id))
        writer.writerow(all_name)
        writer.writerow(all_gmail)
        writer.writerow(all_number1)
        writer.writerow(all_number2)

    print("writed file")
    return 1

def almost_main(lesson_link,write_name):

    all_ids = get_all_student_ids_from_lesson(lesson_link,is_print=False)
    all_names = get_all_student_names_by_id(all_ids, is_print=False)
    all_gmails = get_all_student_gmails_by_id(all_ids, is_print=False)
    all_numbers1 = get_all_student_number1_by_id(all_ids,is_print=False)
    all_numbers2 = get_all_student_number2_by_id(all_ids,is_print=False)

    write_student(
        file_name=str(write_name),
        all_id=all_ids,
        all_name=all_names,
        all_gmail=all_gmails,
        all_number1=all_numbers1,
        all_number2=all_numbers2)

    return 0

lesson_1 = "https://lms.must.edu.mn/Student/Lesson?lcode=S.CE102&tcode=B.ES60&type=students&ltp=c"
lesson_2 = "https://lms.must.edu.mn/Student/Lesson?lcode=S.MT102&tcode=E.MT51&type=students&ltp=c"
lesson_3 = "https://lms.must.edu.mn/Student/Lesson?lcode=F.CN104&tcode=F.CN801&type=students&ltp=c"
lesson_4 = "https://lms.must.edu.mn/Student/Lesson?lcode=S.CD101&tcode=F.PH75&type=students&ltp=c"
lesson_5 = "https://lms.must.edu.mn/Student/Lesson?lcode=F.CN112&tcode=J.TC14&type=students&ltp=c"
lesson_6 = "https://lms.must.edu.mn/Student/Lesson?lcode=S.PT101&tcode=K.PT20&type=students&ltp=c"

# almost_main(lesson_link=lesson_1,write_name="22_s2_les1.csv")
# almost_main(lesson_link=lesson_2,write_name="22_s2_les2.csv")
# almost_main(lesson_link=lesson_3,write_name="22_s2_les3.csv")
# almost_main(lesson_link=lesson_4,write_name="22_s2_les4.csv")
# almost_main(lesson_link=lesson_5,write_name="22_s2_les5.csv")
# almost_main(lesson_link=lesson_6,write_name="22_s2_les6.csv")

