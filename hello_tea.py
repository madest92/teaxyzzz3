import requests

def hello_tea_func():
    response = requests.get('https://app.tea.xyz/')
    print("Hello teaxyzzz3!")
    print("Status teaxyzzz3:", response.url, response.ok)
