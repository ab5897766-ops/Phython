#32
a = {3, 7, 11, 13, 17}
b = {17, 21, 23, 27, 31}

print(a | b) 
print(a & b)  

#33
a = {3, 7, 11, 13, 17}
b = {17, 21, 23, 27, 31}

print(a - b)
print(a ^ b)

#34
a = {3, 7, 11, 13, 17}
b = {21, 23, 27, 31, 33}

a.update(b)
print(a)

#35
a = {100, 200, 300, 400, 500}
b = {400, 500, 600, 700, 800}

x = a.copy()
x.intersection_update(b)
print(x)

y = a.copy()
y.difference_update(b)
print(y)

z = a.copy()
z.symmetric_difference_update(b)
print(z)

#36
a = {100, 200, 300, 400, 500}
b = {100, 200, 300, 400, 500}

if a.issuperset(b) and a.issubset(b):
    print("동시")
elif a.issuperset(b):
    print("상위")
elif a.issubset(b):
    print("부분")

#37
a = {3, 7, 11, 13, 17}
a.add(1000)
a.pop()
print(a)

#38
multiples = {x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0}
print(multiples)