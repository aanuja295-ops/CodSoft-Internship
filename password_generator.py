#Task 3


#Anuja's password generator


import random
import string

def generate_password(length):
    """
    Generates a random password using a combination of letters,
    digits, and punctuation.
    """
    
    

    characters = string.ascii_letters + string.digits + string.punctuation
    
    
    password_chars = random.choices(characters, k=length)
    
   
    return "".join(password_chars)

def main():
    """
    Main function to get user input and display the password.
    """
    print("--- 🔒 Python Password Generator ---")
    
    
    while True:
        try:
            
            length = int(input("Enter the desired password length: "))
            
            if length > 0:
                break  
            else:
                print("Password length must be a positive number. Try again.")
                
        except ValueError:
            print("Invalid input. Please enter a number.")
            
   
    password = generate_password(length)
    
   
    print("\n" + "="*20)
    print(f"Your generated password is:")
    print(f"  {password}")
    print("="*20)


if __name__ == "__main__":
    main()