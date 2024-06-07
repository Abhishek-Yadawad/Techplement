import random
import string

def passgen(passlen):
    if passlen <= 0:
        raise ValueError("Password length must be a positive integer.")
        
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    spl_char = "#$%&'()*+,-./:;<=>?@[]^_'{|}~"
    char = uppercase + lowercase + digits + spl_char
    
   
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(spl_char)
    ]
    
   
    password += random.choices(char, k=passlen - 4)
    
    
    random.shuffle(password)
    return "".join(password)

if __name__ == "__main__":
    try:
        p_len = int(input("Password length?: "))
        print("Password generated:", passgen(p_len))
    except ValueError as e:
        print("Invalid input:", e)
