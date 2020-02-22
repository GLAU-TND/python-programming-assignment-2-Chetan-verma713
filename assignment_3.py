n = int(input('Enter the number :' ))
s = bin(n)
s = s[2:]
a = []
b = 0
for i in s:
    if int(i) == 1:
        b += 1
    if int(i) == 0:
        pass
    if b > 0:
        a.append(b)
print(max(a))
