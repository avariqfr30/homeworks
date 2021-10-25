#Avariq Fazlur Rahman
#2502043002
"""
No. 1
Days Calculator
"""
hours = eval(input("Insert how many hours : "))
minutes = eval(input("Insert how many minutes : "))
seconds = eval(input("Input how many seconds : "))
m = (hours*3600)+(minutes*60)+seconds
days = m / 86400
print("There are", format(days, '.4f'), "days.")

