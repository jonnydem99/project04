from django.shortcuts import render


def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/" + ticker + "/quote?token=pk_f7c3d0d74a06499fbf6aa2d949922047")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        return render(request, 'stocktrader/home.html', {'api': api})

    else:
        return render(request, 'stocktrader/home.html', {'ticker': "Enter a ticker symbol above."})


def about(request):
    return render(request, 'stocktrader/about.html')