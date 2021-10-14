import requests

from api import  *

BASE = 'http://127.0.0.1:1234/'
if __name__ == '__main__':

    response = requests.post(BASE + 'movies')
    response = response.json()

    print(response)