import math
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
#h = int(input("Введіть число h, для якогопотрібно знайти дискретний логарифм"))
h = 19
p = 113
tvir_element = find_primitive_element(p)
print("Твірний елемент:", tvir_element)
porad_group = p - 1
print("Порядок групи:", porad_group)
M = int(math.sqrt(porad_group)) + 1
print("Верхня стеля M =", M)
mal_krok = []
for i in range(M):
    mal_krok.append(pow(tvir_element, i, p))

print("малі кроки:", mal_krok)

g_M = pow(tvir_element, -M, p)
print("елемент для великих кроків g**(-M) =", g_M)

for i in range(porad_group):
    vel_krok = (h * g_M ** i) % p
    if vel_krok in mal_krok:
        i_vel = i
        i_vel_num = vel_krok
        break

for i in range(len(mal_krok)):
    if mal_krok[i] == i_vel_num:
        i_mal = i

print("і мале", i_mal)
print("і велике", i_vel)
print("Шуканий дискретний логарифм рівний", i_mal + i_vel*M)