thickness=9
c="H"
for i in range(5):
    print(c.rjust(5-i)+c*(2*i))
for i in range(6):
    print(c.rjust(3)+c*4+c.rjust(13)+c*4)
for i in range(3):
    print(c.rjust(3)+c*24)
for i in range(6):
    print(c.rjust(3)+c*4+c.rjust(13)+c*4)
for i in range(5):
    print(c.rjust(i).rjust(16))
