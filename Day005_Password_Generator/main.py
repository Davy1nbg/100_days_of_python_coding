import random
import string

password_len = 12 

all_signs = string.ascii_letters + string.digits + string.punctuation

new_password = "" 


for i in range(password_len):
    random_sign = random.choice(all_signs)
    # Und wir fügen dieses zufällige Zeichen zu unserem Passwort hinzu
    new_password += random_sign

print("Dein neues Passwort ist:", new_password)