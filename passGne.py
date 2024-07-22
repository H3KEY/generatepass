# Author: h3key
# Version: 1.0
# All credit to h3k3y
import random
import string
import tkinter as tk
from tkinter import filedialog

def passwords(word, quantity):
    special_characters = '@_-*/+.' # you can add or remove characters here
    numbers = string.digits
    similar_passwords = []

    for _ in range(quantity):
        
        modified_word = ''.join(random.choice([char.lower(), char.upper()]) for char in word) 
        modified_word += random.choice(numbers) 
        special_char_pos = random.randint(1, len(modified_word) - 1)
        modified_word = (
            modified_word[:special_char_pos] +
            random.choice(special_characters) +
            modified_word[special_char_pos:]
        )

        # Adjust the length of the word between 8 and 11 characters; you can modify the parameters for more or less length :D
        final_length = random.randint(8, 11)
        while len(modified_word) < final_length:
            modified_word += random.choice(string.ascii_letters + numbers + special_characters)
        
        # Limit the maximum length to 11 characters
        if len(modified_word) > 11:
            modified_word = modified_word[:11]

        similar_passwords.append(modified_word)
    
    return similar_passwords

def select_file_and_save(content):
    root = tk.Tk()
    root.withdraw() 

    file_path = filedialog.asksaveasfilename(
        title="Save file",
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )

    if file_path:
        with open(file_path, 'w') as file:
            for line in content:
                file.write(line + '\n')
        print(f"Generated passwords saved in {file_path}")
    else:
        print("Save canceled.")

# Request base word
base_word = input("Enter the base word: ")
password_quantity = int(input("Enter the number of similar passwords: "))

# Generate similar passwords
generated_passwords = passwords(base_word, password_quantity)

# Save the passwords in a file selected by the user
select_file_and_save(generated_passwords)
