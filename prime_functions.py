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
