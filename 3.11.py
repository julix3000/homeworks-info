"""
# №2 - wzxy

def f(x, y, w, z):
    return not(x <= y) or (not(z) == (w <= x)) or w

print('w', 'z', 'x', 'y')
for x in range(2):
    for y in range(2):
        for w in range(2):
            for z in range(2):
                if not(f(x,y,w,z)):
                    print(w, z, x, y)
"""

"""
#5 - 17

for n in range(1, 100):
    n1 = bin(n)[2:]
    if n%4 == 0:
        n2 = n1 + n1
    else:
        n2 = n1 + n1[::-1]
    
    if int(n2, 2) >= 544:
        print(n)
        break
"""    
    
"""    
# №7 - 17

for n in range(10000):
    if (128*2048 * 11 * n) <= 81920*600:
        print(n)
"""

"""
#8 - 392

al = '123456'
o = '13579'
k = 0

for a in al:
    for b in al:
        for c in al:
            for d in al:
                s = a + b+c + d
                so, se = 0, 0
                for i in s:
                    if i in o: so += 1
                    else: se += 1
                
                if s.count('3') == 1 and se <= so:
                    k += 1
print(k)
"""

"""
# 11 - 138

for n in range(1000000000):
    if 1600 * (((n+1)*9 + 8 - 1)//8) > 244 * 1024:
        print(n)
        break
"""

"""
# 14 - 972
def f(n):
    res = ''
    while n > 0:
        res += (str(n % 6))  
        n //= 6                  
        
    return res[::-1]

s = 6**2025 + 6**25
for x in range(1000, 1, -1):
    t = f(s-x)
    if t.count('0') == 2002:
        print(x)
        break
"""

"""
# 16 - 2500500

f = [0] * 4990
f[1] = 1

for n in range(2, 3001):
    f[n] = n + f[n-1]

print(f[3000] - f[2000])
"""

"""
# 21 - 94

print(88*4)
c = 94 - 3 #p
c = c - 3 #v - <88 || >=91
c = c #p - 88
c = c #v
print(c)

"""


"""
# 23 - 40

f = [0] * 1000
f[3] = 1

for i in range(3, 10):
    f[i + 1] += f[i]
    f[i * 2] += f[i]
    f[i * 3] += f[i]
    
print(f[9])
f = [0] * 1000
f[9] = 4
for i in range(9, 30):
    f[i + 1] += f[i]
    f[i * 2] += f[i]
    f[i * 3] += f[i]
    
print(f[30])
"""
