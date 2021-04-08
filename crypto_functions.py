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
    
    user_inputs = range(a, b + 1)

    prime_numbers_discovered = []

    for inputs in user_inputs:

        prime_return = prime_number_check(inputs)

        if prime_return:
            prime_numbers_discovered.append(inputs)

    return prime_numbers_discovered
