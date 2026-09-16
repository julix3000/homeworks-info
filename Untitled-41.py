
# № 5489 
f = open(r'9_5489.csv')
k = 0
for x in f:
    y = list(map(int, x.split(',')))
    if len(set(y)) == len(y):
        a, b = 0, 0
        c, d = 0, 0
        for i in y:
            if i%2 == 0:
                a += 1
                c += i
            else:
                b += 1
                d += i
        if a > b and c < d:
            k +=1 
print(k)


#№ 5126
k = 0
f = open(r'9_5126.csv')
for x in f:
    y = list(map(int, x.split(',')))
    c = 0
    for i in y:
        if y.count(i) == 3:
            c = i
    if c and len(set(y)) == 4:
        if (sum(y) - 3*c)/3 <= 3*c:
            k += 1
print(k)


#№ 4637
k = 0
f = open(r'9_4637.csv')
for x in f:
    y = sorted(list(map(int, x.split(','))))
    if y[-1]**3 >= 2*y[0]*y[1]*y[2]:
        if y[0] > 10:
            k += 1
print(k)


#4614 
k =0
f = open(r'9_4614.csv')
for x in f:
    y = sorted(list(map(int, x.split(','))))
    if y[-1] < sum(y) - y[-1]:
        if len(set(y)) == 3:
            k += 1
            
print(k)
