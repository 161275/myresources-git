import requests
def fetch_respose(url):
    response = requests.get(url)
    status_code = response.status_code
    print(status_code)
    if status_code == 200:
        add_to_file(response.text)

def add_to_file(txt):
    file_name = "response.txt"
    with open(file_name, "w") as f:
        f.write(txt)


if __name__ == "__main__":
    target_url = "https://jsonplaceholder.typicode.com/users"
    fetch_respose(target_url)