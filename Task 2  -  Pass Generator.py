
import random
import string

def generate_password():
    print("Password Generator")

    # get length from user
    length = input("Enter desired password length: ")
    length = int(length)

    # characters to choose from
    chars = string.ascii_letters + string.digits + string.punctuation

    # build the password
    password = ''
    for i in range(length):
        password += random.choice(chars)

    print("Generated Password:", password)

generate_password()
