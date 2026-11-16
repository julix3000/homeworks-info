# 31510 - 16
"""
def f(a, b):
    if a == b: return 1
    if a > b: return 0
    return f(a+1,b) + (f(int(str(a)[0]+ str(a)[2]+str(a)[1]), b) if str(a)[1] < str(a)[2] else 0)
print(f(100, 141))

def g(a, b):
    f = [0]*10000   
    f[a] = 1
    for i in range(a, b):
        f[i+1]+=f[i]
        if str(i)[1]< str(i)[2]:
            f[int(str(i)[0]+ str(i)[2]+str(i)[1])] += f[i]
    return f[b]
print(g(100, 141))
"""

#31420 - 1888
"""
def f(a, b, e):
    if a > b: return 0
    if a == b: return 1
    
    res =  f(a+1, b, 1) if e!=1 else 0
    res += f(a+3, b, 2) if e!=2 else 0
    res += f(int(str(a).replace('1', '3')), b, 3) if str(a).count('1') and e!=3 else 0
    return res
print(f(11, 94, 0))
"""

# 31229 - 480
"""
def f(a, b):
    if a > b: return 0
    if a == b:return 1
    
    res = f(a+1, b)
    res += f(int(str(a).replace('1', '3')), b) if str(a).count('1') else 0
    return res

print(f(10, 84))
"""

# 31159 - 1408
"""
def f(a, b):
    if a > b: return 0
    if a == b:return 1
    
    res = f(a+1, b)
    res += f(int(str(a).replace('1', '2')), b) if str(a).count('1') else 0
    return res

print(f(11, 92))
"""

# 29353 - 188
"""
def f(a, b):
    if a > b: return 0
    if a == b: return 1
    if a == 14: return 0
    
    return f(a+1, b) + f(a*2,b) + f(a*3, b)
print(f(2, 39))
"""

# 28942 - 80
"""
def f(a, b):
    if a < b: return 0
    if a == b: return 1
    if a == 73: return 0
    
    return f(a-3, b) + f(a-8, b) + f(a//2, b)
print(f(76,41)*f(41,12))
"""

# 27776 - 60
"""
def f(a, b):
    if a < b: return 0
    if a == b: return 1
    
    return f(a-1, b) + f(a//2, b)
print(f(40, 16) * f(16, 6))
"""

# 28764 - 2716
"""
def f(a, b):
    if a > b: return 0
    if a== b: return 1
    if a== 7: return 0
    
    return f(a+1, b) + f(a+3, b) + f(a*2, b)
print(f(2, 15)*f(15, 25))
"""




# 19892 - 364
"""
for x in range(4, 10000):
    if 512 % ((x*1024*1024*8)//(1920*1080*16)) == 52:
        print(x)
        break
"""

# 21406 - 1998000
# print(((3840*2160*17 - 1280*720*5)*120)/8/1024)

# 20804 - 942
"""
for n in range(1000, 1, -1):
    if 1280*960*11 * n / 96468992 <= 132:
        print(n)
        break
"""    
    
# 20538 - 16384
"""
for n in range(25, 1, -1):
    if 640*480 * (n + 10) <= 900 * 1024 * 8:
        print(2**n)
        break
"""    
    
# 16254 - 32
"""    
for n in range(25, 1, -1):
    if 3*1024*1024*8 >= 1600*1200*(10 + n) * 5/6:
        print(n)
        break
"""

# 12723 - 64
"""
for n in range(20, 1, -1):
    if 4.5 * 1024*1024*8 >= 1920*1080*(11 + n + 1):
        print(2**n)
        break
"""

# 9694 - 32
"""
for n in range(50, 0, -1):
    if 1215*1024*8 >= 1920*1080*(n+1)*0.8:
        print(n)
        break
"""

#8944 - 2048
"""
for n in range(50, 0, -1):
    if 3*1024*1024*8 >= 1080*920*(20 + n) * 0.8:
        print(n)
        break
"""
