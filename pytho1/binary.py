num = int(input('Enter values'))
ans = 0
new_num = 0
count = 0
while (num != 0):
    bit = num & 1
    ans = (bit * pow(10, new_num)) + ans
    num = num >> 1
    new_num += 1
print(ans)
number = str(ans)
for i in number:
    if i == '0':
        count += 1
print(count)
