import time

# Simulated user database
users = {
    'adminstaff': {'password': 'admin123'}
}


def brute_force_login(username, password_list):
    for password in password_list:
        print(f"Attempting to login with password: {password}")
        time.sleep(1)  # Simulate delay between attempts

        if users.get(username) and users[username]['password'] == password:
            print(f"Success! Correct password: {password}")
            return True
        else:
            print(f"Failed attempt with password: {password}")

    print("Brute force attack failed.")
    return False


if __name__ == "__main__":
    username = input("Enter username to attack: ")

    # List of passwords to try (in reality, this would be much larger)
    password_list = ['12345', 'password', 'admin123', 'qwerty']

    brute_force_login(username, password_list)
