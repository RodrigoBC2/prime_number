# function to identify if a given number is prime or not.
def prime_number_check(x):
    # defining the least prime number to make a proper range
    if x < 1:
        return False

    else:
        n = 2

        while n * n <= x:
            if x % n == 0:
                return False

            else:
                n += 1

            return True


print("Number to check (must be integer and positive) if it is a prime number or not: ")

x = int(input())

result = prime_number_check(x)

if not result:
    print("The given number", x, "IS NOT a prime number")

else:
    print("The given number", x, "IS a prime number")
