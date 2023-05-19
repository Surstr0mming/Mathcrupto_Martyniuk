
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

p = int(input("Введіть просте число , бінарна довжина якого не більша 20 :"))
while (is_prime(p) != True and int(bin(p)[2:]) >= 20):
    p = int(input("Введіть просте  число, бінарна довжина якого не більша 20 :"))

print("Твірний елемент:", find_primitive_element(p))
