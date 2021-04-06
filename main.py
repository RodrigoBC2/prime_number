from crypto_functions import prime_number_check
from crypto_functions import prime_range


print("If you want just to check if a number is a prime number, type: 1")
print("If you want to know all prime numbers within a given range starting with 1 to any other integer and positive "
      "number, type: 2")

option_type = int(input())

while option_type != 1 or option_type != 2:
    print("If you want just to check if a number is a prime number, type: 1")
    print("If you want to know all prime numbers within a given range starting with 1 to any other integer and "
          "positive number, type: 2")

    option_type = int(input())

if option_type == 1:
    print("Number to check (must be integer and positive) if it is a prime number or not: ")

    x = int(input())

    result = prime_number_check(x)

    if not result:
        print("The given number", x, "IS NOT a prime number")

    else:
        print("The given number", x, "IS a prime number")

else:
    print("Enter 2 integer numbers. The first number can not be zero and the second number must be greater than the first")

    a = int(input())
    b = int(input())

    while a >= b or a == 0:
        print("Enter 2 integer numbers. The first number can not be zero and the second number must be greater than the first")

        a = int(input())
        b = int(input())

    result = prime_range(a, b)

    print("Numbers discovered:", result)
