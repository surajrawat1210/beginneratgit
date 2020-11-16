n=int(input("enter value of n"))
cha=input("enter symbol")
r=" "
for i in range(0,n):
    for j in range(0,n):
        if (((j==1 or j==n//2+2) and i!=0) or ((i==0 or i==n//2) and(j>1 and j<n//2+2))):
            r+=cha
        else :
            r+=" "
    r+="\n"
print(r)