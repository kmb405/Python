for i in range(151):
    print(i)

for i in range(5,1001,5):
    print(i)

for i in range(101):
    if i % 10 == 0:
        print("Coding Dojo")
    elif i % 5 == 0:
        print("Coding")
    else:
        print(i)

sum = 0
for i in range(500000):
    if i % 2 != 0:
        sum += i
print(sum)

for i in range(2018,0,-4):
    print(i)

lowNum = 2
highNum = 20
mult = 3

for i in range(lowNum, highNum, mult):
    print(i)