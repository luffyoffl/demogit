from cryptography.fernet import Fernet
class maskpsw(str):
    def __str__(self):
        return "**********"
    def __rapr__(self):
        return "**********"
def load_key():
    return open("key.txt","rb").read()
def encrypt_password(password):
    key=load_key()
    f=Fernet(key)
    return f.encrypt(password.encode())
def decrypt_password(encrypted_password):
    key=load_key()
    f=Fernet(key)
    hide=f.decrypt(encrypted_password).decode()
    return maskpsw(hide)
def get_password():
    encrypted_password=b'gAAAAABp6NoCUfOM3nELgKlnOgjFj2ABh-eaRC0RVR1OcBwy4nK_3QYzSzgv415EOSN1r6ZskN5G7xYTjlJAGwpZBbqQ9-v5hg=='
    return decrypt_password(encrypted_password)


