from main import prime_number_check

prime_numbers_discovered = []


def prime_range(a, b):

    user_inputs = range(a, b)

    for inputs in user_inputs:

        prime_return = prime_number_check(inputs)

        if prime_return:
            prime_numbers_discovered.append(inputs)

    return prime_numbers_discovered


print("Enter 2 integer numbers. The first number can not be zero and the second number must be greater than the first")

a = int(input())
b = int(input())

while a >= b or a == 0:

    print("Enter 2 integer numbers. The first number can not be zero and the second number must be greater than the first")

    a = int(input())
    b = int(input()) + 1

prime_range(a, b)

print("Numbers discovered:", prime_numbers_discovered)
