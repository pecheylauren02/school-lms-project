def run_insecure_server():
    print("Insecure API is now running.")

    # Simulating non-hashed credentials (INSECURE)
    password = input("Enter password: ")
    mfa_token = input("Enter MFA token: ")

    # Displaying plain text (NOT SAFE)
    print(f"Password: {password}")
    print(f"MFA Token: {mfa_token}")
    print("Insecure server running with plain text credentials.")


if __name__ == "__main__":
    run_insecure_server()
