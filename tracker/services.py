import requests
import json


def fetch_calories(food_name, portion_size):
    query = portion_size + " grams of " + food_name
    print(query)
    api_url = 'https://api.api-ninjas.com/v1/nutrition?query={}'.format(query)
    response = requests.get(api_url, headers={'X-Api-Key': 'w76UQCFkn0sBY6lVS94SqA==ywIXGjhcfHxHE3dN'})

    if response.status_code == requests.codes.ok:
        data = json.loads(response.text)
        if not data:
            return None, "Food not found in the database."
        calories = data[0]['calories']
        return calories, None
    else:
        return None, "API error: {}".format(response.text)