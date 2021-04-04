# function to identify if a given number is prime or not.
def prime_number_check(x):
    # defining the least prime number to make a proper range
    n = 2

    # if the given number is equal to 1 or 2, it is a prime number
    if x == 1 or x ==2:
        print("The given number,", x,", is a prime number")

    else:
        prime = True

        while n*n <= x:
            if x % n == 0 and n != x:
                prime = False
                return prime

            else:
                n += 1

        return prime


print("Number to check (must be integer and positive) if it is a prime number or not: ")

x = int(input())

result = prime_number_check(x)

if result == False:
    print("The given number", x, "IS NOT a prime number")

else:
    print("The given number", x, "IS a prime number")
