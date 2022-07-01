# print swap list
li=list(input("enter list"))
li1 = li[0]
li[0]=li[-1]
li[-1] = li1
print(li)
