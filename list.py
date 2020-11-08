"""Consider a list (list = []). You can perform the following commands:
1. insert i e : Insert integer at position .
2. print: Print the list.
3. remove e : Delete the first occurrence of integer .
4. append e : Insert integer at the end of the list.
5. sort: Sort the list.
6. pop : Pop the last element from the list.
7. reverse : Reverse the list.

Initialize your list and read in the value of followed by lines of commands where each command will
be of the types listed above. Iterate through each command in order and perform the corresponding
operation on your list.
Input Format
The first line contains an integer, , denoting the number of commands.
Each line of the subsequent lines contains one of the commands described above.
Constraints
The elements added to the list must be integers.
Output Format
For each command of type print, print the list on a new line.
"""

if __name__ == '__main__':
    list = []
    n = int(raw_input())
    for i in range(n):
        a = raw_input().split()
        if len(a) == 3:
            eval("list." + a[0] + "(" + a[1] + "," + a[2] + ")")
        elif len(a) == 2:
            eval("list." + a[0] + "(" + a[1] + ")")
        elif a[0] == "print":
            print(list)
        else:
            eval("list." + a[0] + "()")
    
        


















