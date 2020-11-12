'''Designer Door Mat

Mr. Vincent works in a door mat manufacturing company. One day, he designed a new door mat with the
following specifications:
Mat size must be X . ( is an odd natural number, and is times .)
The design should have 'WELCOME' written in the center.
The design pattern should only use | , . and - characters.

Input Format
A single line containing the space separated values of n and m .

 Input :-  7 21
 Output:-
---------.|.---------
------.|..|..|.------
---.|..|..|..|..|.---
-------WELCOME-------
---.|..|..|..|..|.---
------.|..|..|.------
---------.|.---------

'''

n,m=input().split()
x="-"
y=".|."
n,m=int(n),int(m)
j=(m//2)-1
for i in range(n//2):
    print(x*j+(2*i+1)*y+x*j)
    j-=3
print(x*((m-7)//2)+"WELCOME"+x*((m-7)//2))
j+=3
for i in range(n//2-1,-1,-1):
    print(x*j+(2*i+1)*y+x*j)
    j+=3