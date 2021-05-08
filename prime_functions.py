# function to identify if a given number is prime or not.
def prime_number_check(x):
    
    if 1 <= x <= 3:
        return True

    elif x % 2 == 0:
        return  False

    else:
        n = 3
        while n * n <= x:
            if x % n == 0:
                return False

            else:
                n += 2

    return True


# verify and save all prime numbers withing a given range.
def prime_range(a, b):
   
    return [inputs for inputs in range(a,b+1) if prime_number_check(inputs)]


# function to generate prime numbers from a start number to a specific amount greater than the given one.
def generate_primes(from_number, amount):

    found_prime_numbers = []

    while len(found_prime_numbers) < amount:
        if prime_number_check(from_number):
            found_prime_numbers.append(from_number)
        from_number += 1

    return found_prime_numbers


# fuction to give all prime numbers from 1 to the input number
def eratosthenes(limit_input):

    prime_list = [i for i in range(1, limit_input+1)]

    n = 2

    while n*n <= limit_input:
        
        if n in prime_list:
            
            for j in range(n*2, limit_input+1, n):
                if j in prime_list:
                    prime_list.remove(j)

        n += 1

    return prime_list


# function to return True of False for a given entry. If False, the entry number is not prime. If True, its probably prime.
import random

# If False is returned then it is false that n is prime
# if True os returned it is probably true that n is prime
def miller_rabin(n,k):

    if n == 2:
        return True

    if n % 2 == 0:
        return False

    r = 0
    s = 0
    n = -1
    
    # This while loop is infinite
    while s % 2 == 0:
        r += 1
        s //= 2

    # underscore indicates that the for loop variable does not matter, just want to cycle in the loop.
    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, s, n)

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)

            if x == n - 1:
                break

        else:
            return False

    return True
