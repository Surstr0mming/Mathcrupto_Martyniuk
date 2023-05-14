import math
import random


def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


#функція  Ойлера
def fi(n):
    f = n
    if n % 2 == 0:
        while n % 2 == 0:
            n = n // 2
        f = f // 2
    i = 3
    while i * i <= n:
        if n % i == 0:
            while n % i == 0:
                n = n // i
            f = f // i
            f = f * (i - 1)
        i += 2
    if n > 1:
        f = f // n
        f = f * (n - 1)
    return f


def extended_euclidean_algorithm(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_euclidean_algorithm(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


p = random.randint(1, 1000)
while is_prime(p) == False:
    p = random.randint(1, 1000)

q = random.randint(1, 1000)
while is_prime(q) == False:
    q = random.randint(1, 1000)

print("p = ", p)
print("q = ", q)

n = p * q
print("n = p * q = ", n)
# (p-1)(q-1)
#elera_n = fi(n)
elera_n = (p - 1) * (q - 1)
print("fi(n) = ", elera_n)

e = random.randint(2, elera_n - 1)
while math.gcd(e, elera_n) != 1:
    e = random.randint(2, elera_n - 1)
print("e = ", e)

d = extended_euclidean_algorithm(e, elera_n)[1]
if d < 0:
    d += elera_n

print("d = ", d)

message = input("enter secter message : ")
decimals = [ord(c) for c in message]
print(decimals)
print("U entered ", message)

crypto_text = []
for i in decimals:
    crypto_text.append(i ** e % n)

print("crypto text = ", crypto_text)
decrypt_text = ''

for i in crypto_text:
    pivot = i ** d % n
    decrypt_text += chr(pivot)
print("decrypted text equls to ", decrypt_text)
'''
# 2
print("222222")

p = 17
q = 11
e = 7
crypto_text = [15]

q_ob = extended_euclidean_algorithm(q, p)[1]
p_ob = extended_euclidean_algorithm(p, q)[1]
if q_ob < 0:
    q_ob += p

if p_ob < 0:
    p_ob += q
print(q_ob)
print(p_ob)

mas_cp = []
mas_cq = []

for i in range(len(crypto_text)):
    mas_cp.append(crypto_text[i] % p)
    mas_cq.append(crypto_text[i] % q)

print(mas_cp)
print(mas_cq)

mq = []
mp = []

for i in range(len(crypto_text)):
    mq.append(mas_cp[i] ** p_ob % q)
    mp.append(mas_cq[i] ** q_ob % p)

print(mq)
print(mp)

text = []
for i in range(len(crypto_text)):
    text.append((mq[i] * q * p_ob + mp[i] * p * q_ob) % n)

print(text)

'''
