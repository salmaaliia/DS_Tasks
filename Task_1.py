#Task_1

#1

A = False #@param {type:"boolean"} 
B = True #@param {type:"boolean"} 
C = True #@param {type:"boolean"}


#2
s = input()
if len(s) >3:
    print(s[0] + str(len(s[1:len(s)-1])) + s[len(s)-1] )
else:
    print(s)



#3
"""tupe = (1,2,3,4,5,6,7,8,9,10)
list1 =[]
for t in tupe:
    t=2*t
    list1.append(t)"""

tupe = (1,)
for i in range(2,11):
    tupe+=(i,)
#print(tupe)
list1 =[]
for t in tupe:
    t=2*t
    list1.append(t)
#print(list1)


#4
s = "Mansoura"[::-1]
print(s)




#5
"""st = "Friendship is the tree of its seeds tender"
st = st.split(" ")
lis=[]
#print(st)
for s in st:
    lis+=[s[0]]
#print(lis)"""

st = "Friendship is the tree of its seeds tender"
list1 =[word[0] for word in st.split(" ")]
#print(list1)




#6
class car:
    def __init__(self,name, color, age):
        self.name = name
        self.color =color
        self.age = age



#problem 1 
def split_and_join(line):
    line=line.split(" ")
    line="-".join(line)
    return line

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

#problem 2


import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())
    if n%2 !=0:
        print("Weird")
    elif n%2 == 0:
        if  6<=n<= 20:
            print("Weird")
        else:
            print("Not Weird")

#problem 3

a,b,c,d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
e = (a%100)*(b%100)*(c%100)*(d%100)

if (e%100) <10:
    print("0"+ str(e%100))
else:
    print(e%100)

#problem 4

x = input()
y = input()
z = input()
n = input()
x = int(x)
y = int(y)
z = int(z)
n = int(n)

coordinates = [[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if i+j+k != n ]
print(coordinates)

#problem 5 
def swap_case(s):
    result =""
    for i in s:
        if(i.islower()):
            i=i.upper()
            result = result +i
            #print(i)
        else:
            i=i.lower()
            result = result +i
            #print(i)
    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#problem 6

l1, r1, l2, r2 = input().split()

if int(l2)> int(r1) or int(l1)>int(r2):
    print("-1")
else :
    print(max(int(l1), int(l2)),min(int(r1),int(r2)))
