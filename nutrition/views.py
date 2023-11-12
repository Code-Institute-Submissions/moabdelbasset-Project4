from django.shortcuts import render
import json
import requests


# Create your views here.
def nutrition(request):
    if request.method == "POST":
        query = request.POST["query"]
        api_url = "https://api.api-ninjas.com/v1/nutrition?query="
        api_request = requests.get(
            api_url + query,
            headers={"X-Api-Key": "w76UQCFkn0sBY6lVS94SqA==ywIXGjhcfHxHE3dN"},
        )
        try:
            api = json.loads(api_request.content)
            print(api_request.content)

            if not api:
                raise ValueError("No data returned from API")

            # Initialize variables to avoid reference before assignment error
            jog_minutes = yoga_minutes = gym_minutes = walk_minutes = 0

            # Calculate the minutes for different activities
            if api:
                calories = api[0]["calories"]  # Accessing the calories
                jog_minutes = (
                    calories / 300
                ) * 60  # Replace 'some_value' with the appropriate number
                yoga_minutes = (calories / 223) * 60
                gym_minutes = (calories / 483) * 60
                walk_minutes = (calories / 294) * 60

            context = {
                "api": api,
                "jog_minutes": round(jog_minutes),
                "yoga_minutes": round(yoga_minutes),
                "gym_minutes": round(gym_minutes),
                "walk_minutes": round(walk_minutes),
                # ... other context variables ...
            }
        except Exception as e:
            api = "oops! There was an error"
            print(e)
            context = {"api": api}

        return render(request, "nutrition/nutrition.html", context)
    else:
        return render(
            request, "nutrition/nutrition.html", {"query": "Enter a valid query"}
        )
