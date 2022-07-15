import re
string = 'bhavdip_pambhar_working_log_2022_07.xlsx'
check = re.findall('\..*',string)

for i in check:
    if i in '.pdf':
        print('pdf formate')
    elif i in '.text':
        print('text formate')
    elif i in '.xlsx':
        print('xlsx formate')
    else:
        print('Not in formate')