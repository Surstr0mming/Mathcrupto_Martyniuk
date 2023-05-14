import random
import math
mbprime = 0
composite = 0
for number_of_numbers in range(100):
    print(number_of_numbers, ": ")
    number_512_bit = ''
    for i in range(12):
        number_512_bit += str(random.randint(0, 1))

    number_test = int(number_512_bit, 2)
    while (number_test == 1):
        for i in range(12):
            number_512_bit += str(random.randint(0, 1))

        number_test = int(number_512_bit, 2)

    print(number_test)

    number = number_test
    if (number_test % 2 == 0):
        print("number are composite, because it can divide by 2")
        composite += 1
    else:
        comp = 0
        prime = 0
        while (prime == 0):
            number = number_test
            S = 0
            number -= 1
            while (number % 2 == 0):
                number /= 2
                S += 1
            d = int(number)

            a = random.randint(2, number_test - 1)
            while (math.gcd(a, number_test) != 1):
                a = random.randint(2, number_test - 1)

            comp = 0

            x0 = (a ** d) % number_test
            if (x0 == 1 or x0 == number_test - 1):
                print("maybe prime")
                prime == 0
                print("a1 = ", a)
                mbprime += 1
                break

            else:
                for i in range(1, S):
                    x0 = x0 ** 2
                    # print("x0 % number_test", (x0 % number_test))
                    if (x0 % number_test == 1):
                        print("number are composite")
                        prime = 0
                        comp = 1
                        break
                    elif (x0 % number_test == number_test - 1):
                        print("number maybe prime")
                        prime = 0
                        comp = 2
                        break
                if (comp == 0):
                    prime = 1
                    print("number are composite")
                    composite += 1
                print("a2 = ", a)

            if (comp == 1):
                if (comp == 1):
                    composite += 1
                else:
                    mbprime += 1
                break


print("there are ", mbprime, " maybe prime numbers")
print("there are ", composite, " composite numbers")