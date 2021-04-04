# function to identify if a given number is prime or not.
def prime_number_check(x):
    # defining the least prime number to make a proper range
    n = 2

    # if the given number is equal to 1 or 2, it is a prime number
    if x == 1 or x ==2:
        print("The given number,", x,", is a prime number")

    else:
        prime = True

        while n <= x:
            if x % n == 0 and n != x:
                print("Its not a prime number as it is a multiple of",n)
                prime = False
                break

            else:
                n += 1

        if prime == True:
            print("The given number", x, "is a prime number")


print("Number to check (must be integer and positive) if it is a prime number or not: ")

x = int(input())

