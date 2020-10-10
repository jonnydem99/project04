from django.shortcuts import render


def home( request): 
    import requests
    import json

    #pk_f7c3d0d74a06499fbf6aa2d949922047
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_f7c3d0d74a06499fbf6aa2d949922047")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render( request, 'stocktrader/home.html', {'api': api})

def about( request): 
    return render( request, 'stocktrader/about.html')