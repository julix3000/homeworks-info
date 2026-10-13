"""
#24371

f = [0] * 10000
g = [0] * 10000

for n in range(-10, 100):
    g[n] = n
for n in range(0, 102):
    f[n] = g[n-2]

for n in range(100, 5001):
    g[n] = f[n-3] + 1
    f[n] = g[n-2]

print(f[5000])

from functools import lru_cache
@lru_cache
def F(n):
    return G(n-2)
@lru_cache
def G(n):
    if n < 100:
        return n
    return F(n-3) + 1

for n in range(0, 5000):
    F(n)

print(F(5000))

"""
"""
#23756
f = [0] * 20000
g = [0] * 20000

for n in range(-10, 10):
    g[n] = 2 * n
for n in range(10, 15600):
    g[n] = g[n-2] + 1
n1 = 15548

f[n1] = 2* (g[n1-3] + 8)
print(f[n1])

from functools import lru_cache
@lru_cache
def F(n):
    return 2 * (G(n-3) + 8)
@lru_cache
def G(n):
    if n < 10:
        return 2 *n
    return G(n-2) + 1
for n in range(0, n1):
    G(n)
print(F(n1))
"""

#23562
f = [0]*50000
g = [0]*50000

for n in range(-10, 10):
    g[n] = n * 3
for n in range(10, 48000):
    g[n] = g[n-2] + 1
n1 = 47995
f[n1] = g[n1-1]
print(f[n1])

from functools import lru_cache
@lru_cache
def F(n):
    return G(n-1)
@lru_cache
def G(n):
    if n <= 9:
        return 3*n
    return G(n-2) + 1
for n in range(0, 48000):
    G(n)
print(F(n1))
