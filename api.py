import os
from getpass import getpass
from django.conf import settings
from django.contrib.auth.hashers import make_password, check_password

# Manually configure minimal Django settings
settings.configure(
    PASSWORD_HASHERS=[
        'django.contrib.auth.hashers.PBKDF2PasswordHasher',
        'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
        'django.contrib.auth.hashers.Argon2PasswordHasher',
        'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    ]
)

# Simulating a user database with hashed passwords
users = {
    'adminstaff': {'password': make_password('admin123'), 'is_admin': True},
    'normaluser': {'password': make_password('user123'), 'is_admin': False}
}

def check_admin(username):
    return users.get(username, {}).get('is_admin', False)

def login():
    username = input("Enter username: ")
    password = getpass("Enter password: ")
    
    user = users.get(username)
    
    if user and check_password(password, user['password']):
        print(f"Welcome {username}!")
        return username
    else:
        print("Invalid credentials.")
        return None

def run_secure_api():
    print("Running Secure API...")
    os.system('python secure_api.py')

def run_insecure_api():
    print("Running Insecure API...")
    os.system('python insecure_api.py')

def main():
    print("1. Run Secure API\n2. Run Insecure API\n3. Exit")
    choice = input("Choose an option: ")

    if choice == '1':
        username = login()
        if username and check_admin(username):
            run_secure_api()
        else:
            print("Error: Only administrators can run the secure API.")
    elif choice == '2':
        run_insecure_api()
    elif choice == '3':
        print("Exiting...")
        exit()
    else:
        print("Invalid option. Exiting...")

if __name__ == "__main__":
    main()
