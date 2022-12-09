from django.shortcuts import render, HttpResponse
import requests

# 58c0640a
# 2d3a593c8292f0c6dc646b644489e4e5
def index(request):
    query = "cheesecake"
    response = requests.get(
        "https://api.edamam.com/api/recipes/v2?type=public&q="
        + query
        + "&app_id=58c0640a&app_key=2d3a593c8292f0c6dc646b644489e4e5"
    )
    jsonResponse = response.json()
    recipes = jsonResponse["hits"]
    return render(request, "blog/index.html", {"recipes": recipes})


def specific(request):
    return HttpResponse("Specific Page")


def search(request):
    if request.method == "POST":
        searchText = request.POST.get("userText", "")
        response = requests.get(
            "https://api.edamam.com/api/recipes/v2?type=public&q="
            + searchText
            + "&app_id=58c0640a&app_key=2d3a593c8292f0c6dc646b644489e4e5"
        )
        jsonResponse = response.json()
        recipes = jsonResponse["hits"]
        return render(request, "blog/index.html", {"recipes": recipes})

    else:
        return render(request, "blog/index.html")


def about(request):
    return render(request, "blog/about.html")


def contact(request):
    return render(request, "blog/contact.html")
