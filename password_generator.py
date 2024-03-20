import random
import string

length= int(input("Enter the length of the password: "))

if length < 8:
    print("Password length should be at least 8 characters.")
else:
    password_chars = []
    password_chars.append(random.choice(string.ascii_uppercase))
    password_chars.append(random.choice(string.ascii_lowercase))
    password_chars.append(random.choice(string.digits))
    password_chars.append(random.choice(string.punctuation))
    remaining_length = length - 4  # Subtracting 4 for the characters already chosen
    password_chars.extend(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(remaining_length))
    random.shuffle(password_chars)
    generated_password = ''.join(password_chars)

    print("Generated Password:", generated_password)
