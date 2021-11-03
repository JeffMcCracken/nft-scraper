import requests
from bs4 import BeautifulSoup

from django.shortcuts import render

def index(request):
    html_page = requests.get('https://randomearth.io/collections')    

    soup = BeautifulSoup(html_page.text, 'html.parser')
    return render(request, 'app/index.html', {
        'html': html_page
    })