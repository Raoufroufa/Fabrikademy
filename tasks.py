#task3

"""var = []
sum = 0
min = 0
max = 0
i=0
print("enter your 10 numbers:")

while i<10 :
    x= float(input())
    var.append(x)
    if x > max and x > min:
        max = x
    elif x < min:
        min = x
    sum += x
    i += 1

print("your list of 10 numbers is: ", var)
print("the sum of these numbers is: ", sum, ", the min is: ", min, ", and the max is: ", max)"""
 

#task4
yourList = []
var=[]
i= 0
j=0

print("enter the length of your list: ")
length=int(input())
print("enter your numbers:")

while i<length : 
    x = float(input())
    yourList.append(x)
    i += 1
print("your list is: ", yourList)

y = length
while y>0 :
    var.append(max(yourList))
    yourList.remove(max(yourList))
    y -= 1


print("your list after was ordered from the largest number to the smalest number is: ", var)








