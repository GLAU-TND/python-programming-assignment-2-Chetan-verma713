ls = ['chair', 'height', 'racket', 'touch', 'tunic']
ls1 = []
p = ls[0][-1]
for j in ls:
    for i in ls:
        if p == i[0] and i not in ls1:
            ls1.append(i)
            p = i[-1]
print(ls1)
