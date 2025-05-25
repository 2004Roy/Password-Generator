import random


data="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!#$%&'()*+,-./:;<=>?@[\]^_`{|}~" 

alphabets="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

length=int(input("Enter the length of the password : "))




if length < 5:
    print("Password length must be at least 5.")
else:
    # Pick the first character as an alphabet
    first_char = random.choice(alphabets)
    
    # Pick the rest of the characters (length - 1) from the full data set
    remaining_chars = random.sample(data, length - 1)

    # Combine and shuffle only the remaining part if needed
    password = first_char + ''.join(remaining_chars)

    print(f"Your Password is: {password}")