# Avariq Fazlur Rahman - 2502043002
# -L1CC
"""
No 1 : Convert to Days

"""
def convert_to_days():
    def getTimes ():
        hours = float(input("How many hours has it been? : "))
        minutes = float(input("How many minutes has it been? : "))
        seconds = float(input("How many seconds has it been? : "))
        return hours, minutes, seconds
    def toDays (h, m, s):
        return ((h*3600)+(m*60)+(s))/86400
    h, m, s = getTimes()
    days = toDays(h, m, s)
    
    print ("It has been", format(days, '.4f'), "days.")
convert_to_days()
        
        
