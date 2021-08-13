import requests
from bs4 import BeautifulSoup
import datetime
from datetime import timedelta, date
# url = "https://www.sattamatkagod.net/kalyan-matka-chart.php"
# url = "https://chartkalyan.in/"
url = "https://kalyanpanelchart.in/" #44
r = requests.get(url)
htmlContent = r.content
soup = BeautifulSoup(htmlContent, 'html.parser')
'''------------------------Loop for arrange Data below------------------------'''
def nest_list(list1, rows, columns):
    result = []
    start = 0
    end = columns
    for i in range(rows):
        result.append(list1[start:end])
        start += columns
        end += columns
    return result
'''^^^^^^^^^^^^^^^^^^^^^^^Loop for arrange Data above^^^^^^^^^^^^^^^^^^^^^^^^^'''

''' ----------------------Find all the Numbers Below--------------------------'''
myDataStr= ""
for td in soup.find_all('td')[44:]:#44
    myDataStr += td.get_text()
itemList = myDataStr.split("\n\n")
myString = "".join(itemList)
myString = myString.replace(' ', '')
myString = myString.replace('\n', '')

sepString=""
for i in range(len(myString)):
    if i%2!=0 and i!=len(myString)-1:
        sepString+=myString[i]+","
    else:
        sepString+=myString[i]
DataList = sepString.split(',')

finalDataList = []
for num in DataList:
        index=2
        if num.isdigit():
            finalDataList.append(int(num))
        else:
            finalDataList.append(num)
AllNumberList = nest_list(finalDataList, (len(finalDataList) / 6).__ceil__(), 6)
''' ----------------------Find all the Numbers above-------------------------'''

''' -----------------------Find all the Dates below--------------------------'''
myDataTH= ""
for th in soup.find_all('th')[7:]:#7
    myDataTH += th.get_text()
myDataTH = myDataTH.replace(' ', '')
myDataTH = myDataTH.replace('\n', '')
myDataTH = myDataTH.replace('/', '-')
Dates =""
for index in range(len(myDataTH)):
    if myDataTH[index] =='t':
            rawDates = myDataTH[index-8:index]
            if rawDates[0]=='-':
                Dates+=myDataTH[index-10:index]+" "
            else:
                Dates += myDataTH[index - 8:index] + " "
dateList = Dates.split(' ')
dateList.pop()
arrangedDate = []
for itrate in range(len(dateList)):
    if len(dateList[itrate]) == 8:
        arrangedDate.append(str(dateList[itrate][0:6])+"20"+str(dateList[itrate][6:]))
    else:
        arrangedDate.append(dateList[itrate])
# print(arrangedDate)
finalDate =[]
for datestr in arrangedDate:
    day, month, year =datestr.split('-')
    day_name = datetime.date(int(year), int(month), int(day))
    finalDate.append(day_name.isoformat())
    if arrangedDate.index(datestr)!= len(arrangedDate)-1:
        for k in range(1, 6):
            finalDate.append((day_name+datetime.timedelta(k)).isoformat())
AllDateList = nest_list(finalDate, (len(finalDate) / 6).__ceil__(), 6)

if(len(AllNumberList[len(AllNumberList) - 1])>len(AllDateList[len(AllDateList) - 1])):
    year1, month1, day1 = AllDateList[len(AllDateList)-1][len(AllDateList[len(AllDateList)-1])-1].split('-')
    day_name1 = datetime.date(int(year1), int(month), int(day1))
    for v in range(len(AllNumberList[len(AllNumberList) - 1])-1):
        AllDateList[len(AllDateList) - 1].append((day_name1+datetime.timedelta(v+1)).isoformat())
'''^^^^^^^^^^^^^^^^^^^^^^^^Find all the Dates above^^^^^^^^^^^^^^^^^^^^^^^^^^^^'''

for d in AllNumberList:
    print(d)




