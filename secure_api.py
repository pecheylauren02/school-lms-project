import hashlib
import hmac


def hash_data(data, secret_key="supersecret"):
    return hmac.new(secret_key.encode(), data.encode(),
                    hashlib.sha256).hexdigest()


def run_secure_server():
    print("Secure API is now running.")

    # Simulating hashed credentials (SAFE)
    password = input("Enter password: ")
    mfa_token = input("Enter MFA token: ")

    hashed_password = hash_data(password)
    hashed_mfa_token = hash_data(mfa_token)

    print(f"Hashed Password: {hashed_password}")
    print(f"Hashed MFA Token: {hashed_mfa_token}")
    print("Secure server running with hashed credentials.")


if __name__ == "__main__":
    run_secure_server()
