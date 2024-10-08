# 1 Password generator

import random
import string

def generate_password(length):
    # Define the character pool: lowercase, uppercase, digits, and special characters
    characters = string.ascii_letters + string.digits + string.punctuation

    # Randomly select characters from the pool to create a password of the desired length
    password = ''.join(random.choice(characters) for i in range(length))

    return password

def main():
    print("Password Generator")

    while True:
        try:
            length = int(input("Enter the desired length of the password: "))
            if length <= 0:
                print("Please enter a positive number.")
                continue
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        generated_password = generate_password(length)
        print(f"Generated Password: {generated_password}")

        again = input("Do you want to generate another password? (yes/no): ").lower()
        if again != 'yes':
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
