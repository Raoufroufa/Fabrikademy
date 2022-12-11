print ("choose the state of the weather: rainy, sunny, or other")
x= input() 
if x== "sunny" :
  print ("enter the value of the weather temperature :")
  y= input()
elif x== "rainy" :
  print("do you have electricity at home? enter only yes or no")
  power= input()
else :
    print("It is up to you to make the decision")
if (x== "rainy") and (power== "yes") :
    print("you have to stay at home and watch Netflix")
elif (x== "rainy") and (power== "no") :
    print("you have to stay at home and read a novel")
elif (x== "sunny") and (y>= "28") :
    print("you can go out and vist the mall")
elif (x== "sunny") and (y< "28") :
    print("you can go out and visit the garden")
