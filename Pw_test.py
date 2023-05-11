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

additional_ids = ['B161350491 ','B170910823 ','B170930006 ','B170930802 ','B171020070 ','B171320077 ','B171340925 ','B180220064 ','B180420233 ','B180600012 ','B180900031 ','B180930103 ','B180950022 ','B180960034 ','B181030446 ','B181040006 ','B181060302 ','B181070014 ','B181100416 ','B181350376 ','B181350990 ','B190930015 ','B190930043 ','B190930122 ','B190930130 ','B190950006 ','B190950014 ','B190960014 ','B190960019 ','B190970013 ','B191020001 ','B191020028 ','B191030418 ','B191030421 ','B191910803 ','B191940100 ','B200900015 ','B200900035 ','B200900036 ','B200900802 ','B200910844 ','B200910850 ','B200920049 ','B200920807 ','B200930817 ','B200930831 ','B200960020 ','B200970307 ','B200970312 ','B201030266 ','B201070009 ','B201100360 ','B201270118 ','B201280014 ','B201300023 ','B201350341 ','B201350756 ','B210420028 ','B210600027 ','B210770060 ','B210790009 ','B210900026 ','B210900052 ','B210900802 ','B210900803 ','B210900804 ','B210900806 ','B210910008 ','B210910012 ','B210910048 ','B210910085 ','B210910805 ','B210910808 ','B210910811 ','B210910818 ','B210910819 ','B210910822 ','B210910826 ','B210910828 ','B210910841 ','B210910842 ','B210910846 ','B210910847 ','B210910850 ','B210910853 ','B210910854 ','B210910855 ','B210910858 ','B210910859 ','B210910860 ','B210910863 ','B210910869 ','B210920012 ','B210920801 ','B210920803 ','B210930019 ','B210930804 ','B210930813 ','B210930816 ','B210930819 ','B210930820 ','B210930835 ','B210930840 ','B210930843 ','B210960001 ','B210970051 ','B210970056 ','B210970114 ','B210970404 ','B210970407 ','B210970408 ','B210970409 ','B210970410 ','B210970412 ','B210970413 ','B211020041 ','B211030203 ','B211030204 ','B211040012 ','B211050236 ','B211070001 ','B211070043 ','B211070079 ','B211270007 ','B211270200 ','B211320064 ','B211340017 ','B211340123 ','B211340128 ','B211340133 ','B211340601 ','B211350129 ','B211350155 ','B211350178 ','B211350288 ','B211350354 ','B211350369 ','B211890010 ','B211890803 ','B211900047 ','B211900400 ','B211900802 ','B211910010 ','B211910804 ','B211930041 ','B211940016 ','B211940023 ','B220610014 ','B221340007 ','B221400004 ','B221400007 ','B221630009 ','B221640007 ','B221680004 ','B221740006 ','B221860001 ','B221860004 ','B221860006 ','B221860007 ','B221860008 ','B221860011 ','B221860015 ','B221860017 ','B221860018 ','B221860019 ','B221860020 ','B221860023','B221860023 ','B221860024 ','B221860025 ','B221860027','B221860027 ','B221860029','B221860031','B221860031 ','B221870001','B221870002','B221870002 ','B221870003 ','B221870004 ','B221870005','B221870008 ','B221870009','B221870010 ','B221870011 ','B221870014 ','B221870015 ','B221870020 ','B221870022 ','B221870026 ','B221870027 ','B221870028 ','B221870029','B221870029 ','B221870031 ','B221870033 ','B221870035 ','B221870036 ','B221870037 ','B221870038 ','B221870039 ','B221870040 ','B221870041 ','B221870044 ','B221870045 ','B221870049 ','B221870052 ','B221870055 ','B221870056 ','B221870057 ','B221870059 ','B221870060 ','B221870061 ','B221870066 ','B221870090 ','B221870101 ','B221880005 ','B221880008 ','B221880011 ','B221880012 ','B221880013 ','B221880015 ','B221880017 ','B221880019 ','B221880022 ','B221880023 ','B221880024 ','B221880027 ','B221880030 ','B221880031 ','B221880032 ','B221880037 ','B221880040 ','B221880041 ','B221880042 ','B221880045 ','B221880060 ','B221890001 ','B221890002 ','B221890004 ','B221890007 ','B221890008 ','B221890009 ','B221890010 ','B221890011 ','B221890012 ','B221890014 ','B221890016 ','B221890018 ','B221890019 ','B221890020 ','B221890021 ','B221890022 ','B221890023 ','B221890026 ','B221890032 ','B221890034 ','B221890035 ','B221890037 ','B221890041 ','B221890042 ','B221890044 ','B221890045 ','B221890047 ','B221890048 ','B221890060 ','B221910003 ','B221910005 ','B221910007 ','B221910008 ','B221910009 ','B221910010 ','B221910013 ','B221910017 ','B221910018 ','B221910021 ','B221910023 ','B221910026 ','B221910028 ','B221910029 ','B221910030 ','B221910031 ','B221910034 ','B221910035 ','B221910037 ','B221910039 ','B221910042 ','B221910046 ','B221910061 ','B221910062 ','B221910070 ','B221930001 ','B221930002 ','B221930005 ','B221930006 ','B221930007 ','B221930008 ','B221930009 ','B221930011 ','B221930014 ','B221930015 ','B221930016 ','B221930021 ','B221930022 ','B221930023 ','B221930025 ','B221930030 ','B221930031 ','B221930042 ','B221930045 ','B221930046 ','B221930048 ','B221930049 ','B221930051 ','B221930054 ','B221930055 ','B221930056 ','B221930070 ','B221930701 ','B221940001 ','B221940002 ','B221940003 ','B221940008 ','B221940009 ','B221940011 ','B221940013 ','B221940014 ','B221940017 ','B221940019 ','B221940021 ','B221940023 ','B221940024 ','B221940025 ','B221940026 ','B221940027 ','B221940029 ','B221940034 ','B221940035 ','B221940037 ','B221940038 ','B221940039 ','B221940040 ','B221940046 ','B221940048 ','B221940049 ','B221940050 ','B221940051 ','B221940052 ','B221940054 ','B221940055 ','B221940061 ','B221940062 ','B221940063 ','B221940064 ','B221940065 ','B221940066 ','B221940067 ','B221940070 ','B221940071 ','B221940072 ','B221940074 ','B221940075 ','B221940076 ','B221940078 ','B221940192 ','B221940193 ','B221940195 ','B221940196 ','B221940197 ','B221940198 ','B221940200 ','B221940301 ','B221940702 ','B221940703 ','B221940704 ','B221950001 ','B221950002 ','B221950004 ','B221950006 ','B221950007 ','B221950008 ','B221950009 ','B221950010 ','B221950014 ','B221950015 ','B221950016 ','B221950018 ','B221950019 ','B221950021 ','B221950022 ','B221950023 ','B221950024 ','B221950025 ','B221950026 ','B221950027 ','B221950030 ','B221950035 ','B221950036 ','B221960001 ','B221960004 ','B221960005 ','B221960006 ','B221960007 ','B221960009 ','B221960010 ','B221960013 ','B221960016 ','B221960018 ','B221960019 ','B221960021 ','B221960022 ','B221960023 ','B221960025 ','B221960028 ','B221960032 ','B221960037 ','B221960038 ','B221960040 ','B221960041 ','B221960060 ','B221990003 ','B221990009 ','B221990012 ','B221990017 ','B221990018 ','B221990511 ','B222050513 ','B222050514 ','B222090006 ','B222100002 ','B222100019 ','B222100505 ','B222120018 ','B222120021 ','B222120030 ','B222120042 ','B222130068 ','B222130074 ','B222130079 ','B222130091 ','B222130121 ','B222140002 ','B222150001 ','B222150017 ','B222170008 ','B222180015 ','B222180050 ','B222190044 ','B222190524 ','B222230003 ','B222230008 ','B222230009 ','B222230013 ','B222230021 ','B222230022 ','B222230024 ','B222230026 ','B222230028 ','B222230030 ','B222230033 ','B222230034 ','B222230037 ','B222230041 ','B222230043 ','B222230047 ','B222230050 ','B222230053 ','B222230056 ','B222230058 ','B222230060 ','B222230061 ','B222230062 ','B222230091 ','B222270006 ','B222270010 ','B222270011 ','B222270014 ','B222270015 ','B222270018 ','B222270020 ','B222270023 ','B222270026 ','B222270027 ','B222270031 ','B222270033 ','B222270035 ','B222270036 ','B222270042 ','B222270045 ','B222270047 ','B222270049 ','B222270050 ','B222270051 ','B222270052 ','B222270054 ','B222270056 ','B222270057 ','B222270058 ','B222270059 ','B222270060 ','B222270061 ','B222270062 ','B222270063 ','B222270065 ','B222270067 ','B222270068 ','B222270072 ','B222270073 ','B222270074 ','B222270075 ','B222270077 ','B222270081 ','B222270082 ','B222270083 ','B222270085 ','B222270086 ','B222270087 ','B222270088 ','B222270089 ','B222270093 ','B222270095 ','B222270097 ','B222270098 ','B222270150 ','B222290001 ','B222290006 ','B222290008 ','B222290009 ','B222290010 ','B222290012 ','B222290014 ','B222290015 ','B222290016 ','B222290018 ','B222290020 ','B222290024 ','B222290025 ','B222290026 ','B222290028 ','B222290034 ','B222290035 ','B222290037 ','B222290051 ','B222290505 ','B222290506 ','B222300001 ','B222300003 ','B222300005 ','B222300006 ','B222300017 ','B222300020 ','B222300030 ','B222300034 ','B222300501 ','B222300505 ','B222300509 ','B222660020 ','B222660039 ','B222660042 ','B222660048 ','B222660053 ','B222660070 ','B222660071 ','B222670029 ','B222680024 ','B222680050 ','B222680051 ','B222690004 ','B222690009 ','B222690018 ','B222710010 ','B222720039 ','B222720043 ','B222720044 ','B222760008 ','B222760013 ','B222760025 ','B222800004 ','B222800009 ','B222800021 ','B222800025 ','B222800041 ','B222800043 ','B222800044 ','B222800052 ','B222800060 ','B222800065 ','B222800071 ','B222800090 ','B222850008 ','B222850024 ','B222870010 ','B222870029 ','B222870052 ','B222870055 ','B222870060 ','B222870107 ','B222870114 ','B222870118 ','B222870128 ','B222870702 ','B222900013 ','B222900016 ','B222920005 ','B222920030 ','B222920036 ','B222930001 ','B222930003 ','B222930013 ','B222930021 ','B222930023 ','B222930024 ','B222930031 ','B223000003 ','B223000006 ','B223000008 ','B223000009 ','B223000010 ','B223000016 ','B223000020 ','B223000021 ','B223000022 ','B223000027 ','B223000028 ','B223000029 ','B223000030 ','B223000031 ','B223040017 ','B223040026 ','B223040027 ','C.GM00D135 ','I.LM13D018 ','J.CS20E050 ','J.ES09D022 ','J.HW07D071 ','J.IT12D800']

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

import csv
with open('eng2.csv', 'w',encoding="utf-8", newline='') as file:
    writer = csv.writer(file)
    
    writer.writerow(list(all_ids))
    writer.writerow(all_names)
    writer.writerow(all_gmails)
    writer.writerow(all_numbers1)
    writer.writerow(all_numbers2)
