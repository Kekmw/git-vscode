input = str(input())
upper = 0
lower = 0
special = 0
num = 0

for i in input:
    if i.isupper():
        upper = upper+1
    if i.islower():
        lower = lower+1
    if i.isnumeric():
        num = num + 1
    else:
        special = special + 1

print("upper = ", upper)
print("lower = ", lower)
print("special =", special)
print("num = ", num)
