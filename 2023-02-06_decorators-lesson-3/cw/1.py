"""↓ personal work ↓ 29"""
find = 100001
top = int(find**1.3)
primes = [True] * top
i = 2
while i ** 2 <= len(primes):
    if primes[i]:
        j = i ** 2
        while j < len(primes):
            primes[j] = False
            j += i
    i += 1
c = 0
for i in range(2, top):
    if primes[i]:
        c += 1
    if c == find:
        print(i)
        break

