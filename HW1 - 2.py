#Avariq Fazlur Rahman
#2502043002
"""
No. 2
Weight calculator
"""
weight = eval(input("Insert you weight : "))
planet = eval(input("Which planet you are in (1 if Earth, 2 if Jupiter) : "))
if planet == 1 :
    g = 9.8
    bodymass1 = weight * (g//9.8)
    print("Your weight on earth is : ", format(bodymass1, '.4f'))
if planet == 2 :
    g = 23.1
    bodymass2 = weight * (g/9.8)
    print ("Your weight on Jupiter is : ", format(bodymass2, '.4f'))