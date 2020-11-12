import textwrap
s=input()
s=textwrap.wrap(s,3)
print(s)
for i in range(len(s)):
    for j in s[i]:
        while s[i].count(j)>1:
            s[i].replace(j,"")
print("hello")
print(s)