# exercise 01
while True:
    input_number = int(input('Enter a number between 1 and 10: '))
    if input_number in range(1, 11):
        total = 0
        for number in range(1, input_number + 1):
            total += number
        print(f'The sum is: {total}')
        break
    else:
        print("Invalid number, try again!")

# exercise 02

input_number = int(input('Enter a number : '))

table = []
for number in range(1, 11):
    new = input_number * number
    table.append(new)
print(table)

# exercise 03

multiples_13_9 = []

for number in range(2950, 5210):
    if number % 13 == 0 and number % 9 == 0:
        multiples_13_9.append(number)
print(multiples_13_9)

# exercise 04

numbers = [45, 27, 86, 23, 16, 10, 82]
evens = 0
odds = 0

for number in numbers:
    if number % 2 == 0:
        evens += 1
    else:
        odds += 1

print(f"This numbers has {evens} even digits and {odds} odd digits")

# exercise 05-1

while True:
    password = input('Create a password between 4 to 6 letters : ')

    if 4 < len(password) < 7 and password.isalpha():
        print('That is correct!')
        break
    else:
        print("Oops That's not correct ! Please Try again  ")

# exercise 05-2

password = input("Enter your password: ")
shift = int(input("Enter the shift: "))

encrypted_password = ""
for char in password:
    if char.isalpha():
        if char.islower():
            encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        else:
            encrypted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
    else:
        encrypted_char = char
    encrypted_password += encrypted_char

print("Encrypted password:", encrypted_password)
