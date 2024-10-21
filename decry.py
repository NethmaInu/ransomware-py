from cryptography.fernet import Fernet
import os 

key = "lAi0w6E7sGfoE95PmF4IBy9h4McB--tL0_XdbjIsnYs="
f = Fernet(key)

def decrypt(filename, key):

    f = Fernet(key)

    with open(filename, "rb") as file:
        encrypted_data = file.read()

    decrypted_data = f.decrypt(encrypted_data)

    with open(filename, "wb") as file:
        file.write(decrypted_data)

for path,subdirs, files in os.walk("./"):
    for name in files:
        filename = os.path.join(path, name)

        if filename == "./decry.py":
            continue
        decrypt(filename,key)
        x = str(filename[:-5])
        os.rename(filename, x)  

