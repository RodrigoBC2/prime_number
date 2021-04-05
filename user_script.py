from main import prime_number_check

print("Enter 2 integer numbers. The second number must be greater than the first")

a = int(input())
b = int(input())

# while loop to guarantee that user enter the values in the correct way
while a >= b:
    print("Enter 2 integer numbers. The second number must be greater than the first")

    a = int(input())
    b = int(input())

# range from the smaller to the greater number.
user_inputs = range(a, b + 1)

# list to save the prime numbers discovered
prime_numbers_discovered = []

# for loop to analyze each number from a to b and save the prime numbers by adding it to the empty list
for inputs in user_inputs:
    prime_return = prime_number_check(inputs)
    if prime_return == True:
        prime_numbers_discovered.append(inputs)

# printing the prime numbers discovered
print("Numbers discovered:", prime_numbers_discovered)
