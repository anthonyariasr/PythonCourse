"""
The original project ask for a program capable of create a name for a beer by asking the user two questions using
the input function and concat them, due to the simplicity of that request I preferred to make a random name generator
using an API.
"""
import requests #pip install request


def generate_name(answer1, answer2):
    print(f"\nThe generated name is \"{answer1} {answer2}\"\n")


if __name__ == '__main__':
    URL = "https://random-word-api.herokuapp.com/word?number=2"
    response = requests.get(URL)
    if response.status_code == 200:
        generate_name(response.json()[0], response.json()[1])
    else:
        print("Error:", response.status_code, response.text)
