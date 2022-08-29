for x in range(0,151,1):
    print(x)

for x in range(5,1001,5):
    print(x)

for x in range(1,101,1):
    if x % 10 == 0:
        print("Coding Dojo")
    elif x % 5 == 0:
        print("Coding") 
    else:
        print(x)

oddsum=0
for x in range (1,500000,2):
    oddsum = oddsum + x
print(oddsum)

for x in range (2018, 0, -4):
    print(x)

low_num = 4
high_num= 50
mult= 6
for x in range (low_num, high_num):
    if x % mult == 0:
        print(x)