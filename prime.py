f = int(input("enter the lower bound"))
l = int(input("enter the upper bound"))
for i in range(f, l):
    ct = 0
    for j in range(2, (int(i / 2)+1)):
        if i % j == 0:
            ct = 1
        if ct == 1:
            break
    if ct == 0 and i != 1:
        print(i)
