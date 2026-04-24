from idlelib.macosx import hideTkConsole

from cryptography.fernet import Fernet
from utill import encrypt_password
def generate_key():
    key=Fernet.generate_key()
    with open("key.txt","wb+") as f:
        f.write(key)
if __name__ == "__main__":

    generate_key()
    password=input("enter your password:")
    encrypted=encrypt_password(password)
    print("copy to utill file")
    print(encrypted)