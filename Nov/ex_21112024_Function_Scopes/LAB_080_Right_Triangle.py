'''Right Triangle Star Pattern
*
**
***
****
*****
'''

for i in range(1,6):
    print("*" * i)

for i in range(1,6):
    for j in range(i):
        print("*", end="")
    print()