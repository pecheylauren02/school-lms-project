def run_insecure_server():
    print("Insecure API is now running.")
    
    # Simulating a login without hashing (UNSAFE)
    password = input("Enter password (not hashed): ")
    mfa_token = input("Enter MFA token (not hashed): ")

    print(f"Password: {password}")
    print(f"MFA Token: {mfa_token}")
    print("Insecure server running with raw credentials.")

if __name__ == "__main__":
    run_insecure_server()