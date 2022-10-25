a = 0
b = 1
c = 1
rang = int(input("length of fibonacci"))

print(a," ")
print(b," ")

for i in range(0,rang,1):
    c = a+b
    print(c," ")
    a = b
    b = c
    
    
    
