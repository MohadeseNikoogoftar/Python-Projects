from cryptography.fernet import Fernet

# def write_key():
#    key = Fernet.generate_key() 
#    with open("./mykey.key", "wb") as f:
#        f.write(key)    
# write_key()

def load_key():
    with open("./mykey.key", "rb") as f:
        return f.read()
    
key = load_key()
fernet = Fernet(key)


def add_pass(username, password):
    with open("./passwords.txt", "a") as f:
        # string => byte(encode)
        encrypted_pass= fernet.encrypt(password.encode()).decode()
        f.write(f"{username}|{encrypted_pass}\n")
    print("ADDED!")
    
def view_pass():
    with open("./passwords.txt", "r") as f:
        for item in f:
            item = item.rstrip()
            username, encrypted_password = item.split("|")
            password = fernet.decrypt(encrypted_password).decode()
            print(f"Username: {username} | Password: {password} \n")
        
    
while True:
    user_input = input("Enter the mode (v: view, a: add, q=quit)")
    
    if user_input == "v":
        print("your passwords are as follows:")
        view_pass()
        
    elif user_input == "a":
        print("let's add a new yousername-password")
        username= input("Enter new username: ")
        password= input("Enter new password: ")
        add_pass(username, password)
        
    elif user_input == "q":
        break
    else:
        print("wrong mode!")