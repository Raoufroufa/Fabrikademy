
var = list(("a", "b", "c", 2, "6", "8", "w", "t", "e", "r", 9, "r", "57", "q"))
print("enter your charcter: ")
x= input()
y = 0
for i in var :
    if (str(i) == x) :
        y += 1


if y > 0 :
    print("your charcter is found ", y, " times")
else :
    print("your charcter doesn't exist")

