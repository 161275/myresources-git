from typing import Final
import requests

API_KEY: Final[str] = 'ee3baa3933346207f302d6ae9ea25d7a668dc'
BASE_URL: Final[str] = 'https://cutt.ly/api/api.php'




def shorten_url(full_link: str):
    payload: dict = {'key': API_KEY, 'short': full_link}
    response = requests.get(BASE_URL, params=payload)
    data: dict = response.json()
    # print(data)
    # print(data['url'])

    if data['url']['status'] == 7:
        print(data['url']['shortLink'])
    else:
        print("Error status:", data['url']['status'])


    





def main():
    inp_url = str(input("enter a url:"))
    shorten_url(inp_url)






if __name__ == '__main__':
    main()