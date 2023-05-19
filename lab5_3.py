import math
import random
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def find_primitive_element(p):
    for a in range(2, p):
        is_primitive = True
        for i in range(1, p - 1):
            if pow(a, i, p) == 1:
                is_primitive = False
                break
        if is_primitive:
            return a
    return None
'''
p = int(input("Введіть просте число p:"))
while (is_prime(p) != True ):
    p = int(input("Введіть просте число p:"))
'''
p = 467
tvir_element = find_primitive_element(p)
print("Твірний елемент:", tvir_element)
N = p - 1
key_Alice = random.randint(1, 1000000000000)
key_Bob = random.randint(1, 1000000000000)
print("секретний ключ Боба", key_Bob)
print("Секретний ключ Аліси", key_Alice)

X_Alice = pow(tvir_element, key_Alice, p)
Y_Bob = pow(tvir_element, key_Bob, p)
print("X =",X_Alice)
print("Y =",Y_Bob)

S_Bob = pow(Y_Bob, key_Alice, p)
S_Alice = pow(X_Alice, key_Bob, p)
print(S_Alice)
print(S_Bob)