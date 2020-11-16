char=input("enter character like(*)")
n=int(input("enter value of n"))
for i in range(n):
    for j in range(n):
        if (j<1 and i<n//2) or (j>n-2 and i>n//2) or (i==0 or i==n//2 or i==n-1):
            print(char,end="")
        else:
            print(" ",end="")
    print()
    