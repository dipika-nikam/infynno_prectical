from datetime import datetime
import json
from datetime import date
from dateutil import parser

m = []
cout = 0
sort_age = []
f = open('data.json')
data = json.load(f)
for i in data['data']:
    for key, val in i.items():
        if key == 'birth_date':
            DT = parser.parse(val)
            i['birth_date'] = DT.strftime("%d %b %Y")
            to_day = date.today()
            ae = to_day.year - DT.year - ((to_day.month, to_day.day) < (DT.month, DT.day))
            i['employee_age'] = ae

for j in data['data']:
    m.append(j)
c = 0


def next(c):
    for i in data["data"][c:c + 5]:
        print(i)
    return



while True:

    print('1. data in pages')
    print('2. bod sort data')
    print('3. Sort by name')
    print('4. sort by age')
    print('5. exit')
    opti = input('what you want')
    if opti == '1':
        while True:
            print('Pre..1..2..3..4..5..Next')
            option = input('Enter data number')

            if option == "1":
                for i in m[0:5]:
                    print(i)
            elif option == "2":
                for i in m[6:10]:
                    print(i)
            elif option == "3":
                for i in m[11:15]:
                    print(i)
            elif option == "4":
                for i in m[16:20]:
                    print(i)
            elif option == "5":
                for i in m[20:25]:
                    print(i)
            if option == 'N':
                c += 5
                next(c)
                if c == 25:
                    print('Data Over')
                    break
            if option == 'P':
                if c != 0:
                    c -= 5
                    next(c)
                else:
                    print('Not any Previous data')
            if option not in 'P' and 'N':
                print('Please enter P or N Or 1 to 5 ')

    elif opti == '2':
            mo=[]
            data['data'].sort(key = lambda x: datetime.strptime(x['birth_date'], '%d %b %Y'))
            for j in data['data']:
                    new_dic=list(j.items())
                    mo.append(new_dic)

            while True:
                print('Pre..1..2..3..4..5..Next')
                option = input('Enter data number')

                if option == "1":
                    for pach in mo[0:5]:
                        print(pach)
                elif option == "2":
                    for pach in mo[6:10]:
                        print(pach)
                elif option == "3":
                    for pach in mo[11:15]:
                        print(pach)
                elif option == "4":
                    for pach in mo[16:20]:
                        print(pach)
                elif option == "5":
                    for pach in mo[21:25]:
                        print(pach)
                if option == 'N':
                    c += 5
                    next(c)
                    if c == 25:
                        print('Data Over')
                        break
                if option == 'P':
                    if c != 0:
                        c -= 5
                        next(c)
                    else:
                        print('Not any Previous data')
                if option not in 'P' and 'N':
                    print('Please enter P or N Or 1 to 5 ')

    elif opti == "3":
           data['data'].sort(key = lambda x:x['employee_name'])
           print(data['data'])


    elif opti=='4':
        data['data'].sort(key=lambda x: x['employee_age'])
        print(data['data'])

    elif opti =='5':
        n = int(input('Enter age1 range'))
        z = int(input('Enter age2 range'))
        for i in range(len(data["data"])):
            if data["data"][i]["employee_age"] < n :
                if data["data"][i]["employee_age"] > z:
                    print(data["data"][i])

    else:
        continue
