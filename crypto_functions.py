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
   
    return prime_numbers_discovered = [prime_number_check(inputs) for inputs in range(a, b+1)]


# Function to cipher a message (caesar method) using a key (n)
def caesar_cipher(original_text, n):
    
    # Array to save ascII numbers from the text
    transform_asc_ii = [ord(i) for i in original_text]

    # Equation to transform the original text to ciphered text: E(x) = (x + N)
    cipher_asc_ii = [transform_asc_ii[transform_asc_ii.index(x)] + n for x in transform_asc_ii]
    
    # Transforming ascII ciphered text to alphabet form
    caesar_message = [chr(i) for i in cipher_asc_ii]
    
    # join method to deliver the message as suppose to be, since it was in a list.
    return ''.join(caesar_message)


# Function do decipher a given message using the same key as before (n)
def caesar_decipher(caesar_text, n):

    transform_asc_ii = [ord(i) for i in caesar_text]

    # E(x) = (x + N)
    original_asc_ii = [transform_asc_ii[transform_asc_ii.index(x)] - n for x in transform_asc_ii]

    original_message = [chr(i) for i in original_asc_ii]

    return ''.join(original_message)
