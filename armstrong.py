arm = int(input("enter a number"))
sum = 0
temp = arm
if (arm // 1000) < 1:
    while temp > 0:
        digit = temp % 10
        sum = sum + (digit ** 3)
        temp //= 10
else:
    while temp > 0:
        digit = temp % 10
        sum = sum + (digit ** 4)
        temp //= 10
if sum == arm:
    print(1)
else:
    print(-1)

