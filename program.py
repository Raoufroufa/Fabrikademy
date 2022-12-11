print("enter the first number:")
x= input()
print("enter the second number:")
y= input()
print("enter the operator:")
z= input()

if (z == "+") :
    s = int(x) + int(y)
    z = "addition"
elif (z == "-") :
    s = int(x) - int(y)
    z = "subtraction"
elif (z == "*") :
    s = int(x) * int(y)
    z = "multipliction"
else :
    s = int(x) / int(y)
    z = "division"

print("the result of", z, "is", s)
