#!/usr/bin/python
a = 0
def f(x):
    global a
    if (x == 1000):
        a += 11
    elif (x > 99):
        a +=7
        eval_ones(x/100)
        eval_tens(x%100, 3)
    else:
        eval_tens(x,0)

def eval_ones(y):   #count the hundreds and ones
    global a
    if(y== 1 or y==2 or y==6):
        a +=3
    elif(y==3 or y==7 or y==8):
        a +=5
    elif(y==4 or y==5 or y==9):
        a +=4

def eval_tens(z, count_and):   #count the tens
    global a
    if(z==0):
        return
    a+=count_and
    if(z<20):
        if(z== 1 or z==2 or z==6 or z==10):
            a +=3
        elif(z==3 or z==7 or z==8):
            a +=5
        elif(z==4 or z==5 or z==9):
            a +=4
        elif(z==11 or z==12):
            a +=6
        elif(z==15 or z==16):
            a +=7
        elif(z==13 or z==14 or z==18 or z==19):
            a +=8
        elif(z==17):
            a +=9
    else:
        tens = z/10
        if(tens==5 or tens==6 or tens==4):
            a+=5
        elif(tens==2 or tens==3 or tens==8 or tens==9):
            a+=6
        elif(tens==7):
            a+=7
        eval_ones(z%10)


for x in range(1,1001):
    f(x)

print "total: " + str(a)

#  one    3
#  two    3
#  three  5
#  four   4
#  five   4
#  six    3
#  seven  5
#  eight  5
#  nine   4
#  ten    3
#  eleven 6
#  twelve 6
#  thirteen   8
#  fourteen   8
#  fifteen    7
#  sixteen    7
#  seventeen  9
#  eighteen   8
#  nineteen   8
#  twenty     6
#  twenty one
#  ...
#  thirty     6
#  thirty one
#  ...
#  forty     5
#  forty one
#  ...
#  fifty      5
#  fifty one
#  ...
#  sixty      5
#  sixty one
#  ...
#  seventy    7
#  seventy one
#  ...
#  eighty     6
#  eighty one
#  ...
#  ninety     6
#  ninety one
#  ...
#  one hundred    3 + 7    
#  ...
#  one thousand   3 + 8
