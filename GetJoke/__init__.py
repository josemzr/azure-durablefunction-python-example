import requests

def main(name: str) -> str:
    response = requests.get('https://api.chucknorris.io/jokes/random')
    joke = response.json().get('value')
    return joke
