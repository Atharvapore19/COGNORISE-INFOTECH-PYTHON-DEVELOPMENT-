import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    try:
        length = int(input("Enter the desired length of the password: "))
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        
        password = generate_password(length)
        print("Generated password:", password)
    except ValueError as ve:
        print("Error:", ve)
