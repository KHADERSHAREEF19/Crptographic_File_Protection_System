from cryptography.fernet import Fernet

#Generate a random encryption key
def generate_key():
    return Fernet.generate_key()

#save the encrypted key to the file
def save_key(key,key_file):
    with open(key_file, "wb") as file:
        file.write(key)
        
#load the encryption key from the file
def load_key(key_file):
    with open(key_file, 'rb') as file:
        data = file.read()
        
#encrypt a file
def encrypt_file(input_file,output_file,key):
    with open(input_file,'rb') as file:
        data = file.read()
        
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(data)
    
    with open(output_file,'wb') as file:
        file.write(encrypted_data)
        
#decrypt a file
def decrypt_file(input_file,output_file,key):
    with open(input_file,'rb') as file:
        encrypted_data = file.read()
        
    fernet = Fernet(key)
    decrypted_data =fernet.decrypt(encrypted_data)
    
    with open(output_file, 'wb') as file:
        file.write(decrypted_data)
        
#usage
if __name__ == "__main__":
    key = generate_key()
    key_file = 'encryption_key.key'
    save_key(key,key_file)
    
    input_file = 'plaintext.txt'
    encrypted_file = 'encryptedfile.txt'
    decrypted_file = 'decrypted_file.txt'
    
    encrypt_file(input_file,encrypted_file,key)
    print(f"File'{input_file}' encrypted to '{encrypted_file}'")
    
    decrypt_file(encrypted_file,decrypted_file,key)
    print(f"File'{encrypted_file}' decrypted to '{decrypted_file}'")
    