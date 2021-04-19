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


# Function to cipher a message (caesar method) using a key (n)
def caesar_cipher(original_text, n):
    
    # Array to save ascII numbers from the text
    transform_asc_ii = [ord(i) for i in original_text]

    # Equation to transform the original text to ciphered text: E(x) = (x + N)
    cipher_asc_ii = [x + n for x in transform_asc_ii]
    
    # Transforming ascII ciphered text to alphabet form
    caesar_message = [chr(i) for i in cipher_asc_ii]
    
    # join method to deliver the message as suppose to be, since it was in a list.
    return ''.join(caesar_message)


# Function do decipher a given message using the same key as before (n)
def caesar_decipher(caesar_text, n):

    transform_asc_ii = [ord(i) for i in caesar_text]

    # E(x) = (x + N)
    original_asc_ii = [x - n for x in transform_asc_ii]

    original_message = [chr(i) for i in original_asc_ii]

    return ''.join(original_message)


def decipher_input(ciphered_input):
    decrypted_text = None
    valid_text = None
    max_score = 0
    score = 0

    file = open("words.txt", "r")

    # make sure that any punctuation would not interfere when comparing the decrypted text with the words
    all_words = [word.upper().replace('\n', '') for word in file]

    # cycling through all english alphabet rotations to identify witch rotation makes sense
    for i in range(0,26):
        decrypted_text = caesar_decipher(ciphered_input, i).upper()

    # cleaning the punctuations on the decrypted text and compare it with the words of txt file.
        for word in decrypted_text.split(' '):
            word_without_punctuation = ''.join(ch for ch in word.upper() if ch not in set(string.punctuation))
            if word_without_punctuation in all_words:
                score += 1

    # if the words are founded, then the decrypted text is saved as the last known possibility and the amount of words founded to.
        if score > max_score:
            max_score = score
            valid_text = decrypted_text

    return valid_text
