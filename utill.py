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
    encrypted_password=b'gAAAAABp65OEcrLz7AjPjKz7hck76-B-mn_W_Uf2UIsx3KgaPKzjuNu-0rFUg_b3NFqEhh7qd6DvqlJGJafapA8P3DzuMl09ow=='
    return decrypt_password(encrypted_password)


