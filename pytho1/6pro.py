
string = input("Enter string")
char = input("Search charter")
i = 0
count = 0

while (i < len(string)):
    if (string[i] == char):
        count = count + 1
    i = i + 1

print("char of {} is Occurred {} ".format(char,count))