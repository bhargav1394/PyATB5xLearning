'''Left Triangle Star Pattern
*****
****
***
**
*
'''
a = 6
for i in range(a,0,-1):
    i -= 1
    print("*" * i)

for i in range(5,0,-1):
    for j in range(i):
        print("*", end="")
    print()