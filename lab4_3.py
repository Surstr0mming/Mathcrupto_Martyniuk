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

bit_n = bin(n)[2:]
len_n = len(bit_n)
print("bit_n = ", bit_n)
print("len(bit)", len(bit_n))

#m = input("Введіть повідомлення :")
m = "abc"
print("Ви ввели : ", m)

crypto_text = []
for i in m:
    crypto_text.append(bin(ord(i))[2:])

print(crypto_text)
r_mas = []
k0_mas = []
k1_mas = []
decrypt_mas = []
uncrypt_mas = []
uncrypt_message = ''

for i in crypto_text:

    k1 = "0" * random.randint(3, (len_n - len(i) + 1))
    r = ''.join(random.choice(['0', '1']) for _ in range(len_n - len(i) - len(k1)))
    while (len(r) == 0):
        k1 = "0" * random.randint(1, (len_n - len(i) + 1))
        r = ''.join(random.choice(['0', '1']) for _ in range(len_n - len(i) - len(k1)))

    k0 = len(r)
    k0 = 4
    k1 = "000"
    r = "0110"

    r_mas.append(r)
    k0_mas.append(k0)
    k1_mas.append(k1)
    print("r = ", r)
    print("k1 = ", k1)
    print("k0 = ", k0)
    i += k1
    print(i, " = i1")
    decrypt_mas.append(i)

    #хеш функція g
    if (len(r) < len(i)):
        for i_r in range(len(i) - len(r)):
            r += r[i_r % len(r)]
        print(r, " = g(r)")
    elif (len(r) > len(i)):
        len_if = len(r) - len(i)
        r = r[:len(r) - len_if]
        print(r, " = g(r)")
    else:
        print(r, " = g(r)")


    X = ''.join(str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(r, i))
    print(X, " - XOR")
    #друга хеш функція
    X2 = ''
    if(len(X) == k0):
        X2 = X
    else:
        for i_v in range(k0):
            if (int(X[i_v]) + int(X[i_v + 1]) == 2):
                X2 += '0'
            elif (int(X[i_v]) + int(X[i_v + 1]) == 1):
                X2 += '1'
            else:
                X2 += '0'
    #фунція яка скорочує довдину рядка після першої хеш функції до K0 бітів
    #беремо перший плюс другий, другий плюс третій, ...
    print(X2, " друга хеш функція")

    Y = ''
    for i_c in range(len(X2)):
        if (int(X2[i_c]) + int(r[i_c]) == 2):
            Y += '0'
        elif (int(X2[i_c]) + int(r[i_c]) == 1):
            Y += '1'
        else:
            Y += '0'

    print(Y, "Y")

    mes_rsa = X + Y

    print(mes_rsa, "X + Y")

    dec_number = int(mes_rsa, 2)
    print(dec_number, " повідовлення для входу в RSA")

    uncrypt_mas.append(dec_number**e%n)
    ttt = dec_number**e%n
    print("un1 ", ttt)
    #розшифрування

    lettter_mod = bin(ttt**d%n)[2:]
    print("letter_mod = ", lettter_mod)
    start_letter_X = lettter_mod[:len(lettter_mod) - k0]
    fin_letter_Y = lettter_mod[len(lettter_mod) - k0:]
    print("X = ", start_letter_X)
    print("Y = ", fin_letter_Y)
    dec_X = ''
    if (len(start_letter_X) == len(fin_letter_Y)):
        dec_X = fin_letter_Y
    else:
        for i_p in range(len(fin_letter_Y)):
            if (int(start_letter_X[i_p]) + int(start_letter_X[i_p + 1]) == 2):
                dec_X += '0'
            elif (int(start_letter_X[i_p]) + int(start_letter_X[i_p + 1]) == 1):
                dec_X += '1'
            else:
                dec_X += '0'

    dec_r = ''
    for i_f in range(len(dec_X)):
        if (int(dec_X[i_f]) + int(fin_letter_Y[i_f]) == 2):
            dec_r += '0'
        elif (int(dec_X[i_f]) + int(fin_letter_Y[i_f]) == 1):
            dec_r += '1'
        else:
            dec_r += '0'

    r_fin= ''
    if (len(fin_letter_Y) < len(start_letter_X)):
        for i_r in range(len(start_letter_X)):
            r_fin += str(dec_r[i_r % len(fin_letter_Y)])
    else:
        r_fin = dec_r

    mes_with_0 = ''.join(str(int(bit1) ^ int(bit2)) for bit1, bit2 in zip(start_letter_X, r_fin))

    mes_without_0 = mes_with_0[:len(mes_with_0) - len(k1)]
    ascii_mes = int(mes_without_0, 2)
    print("ascii ", ascii_mes)
    uncrypt_message += chr(ascii_mes)
    print(chr(ascii_mes))
    print(uncrypt_message)

print(uncrypt_message, "message")



