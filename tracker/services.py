import requests
import json


def fetch_calories(food_name, portion_size):
    query = portion_size + " grams of " + food_name
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': 'w76UQCFkn0sBY6lVS94SqA==ywIXGjhcfHxHE3dN'})

    if response.status_code == requests.codes.ok:
        data = json.loads(response.text)
        calories = data[0]['calories']
        return calories
    else:
        print("Error:", response.status_code, response.text)