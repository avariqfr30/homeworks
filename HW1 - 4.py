#Avariq Fazlur Rahman - 2502043002
#L1CC
"""
No. 4

"""
def calc_new_height():
    def getHtandWt():
        w1 = eval(input("Input current width : "))
        h1 = eval(input("Input current height : "))
        w2 = eval(input("Input new weight : "))
        return w1, h1, w2
        
    def calcH2(w1,h1,w2):
        return (w2*h1)/w1
    
    w1,h1,w2 = getHtandWt()
    h2 = calcH2(w1, h1, w2)
    print ("The new height is : ", h2)
    
calc_new_height()
        
