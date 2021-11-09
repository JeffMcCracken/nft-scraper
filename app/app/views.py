import requests
from selenium import webdriver

from django.shortcuts import render

def index(request):
    driver = webdriver.Chrome()
    driver.get('https://randomearth.io/collections')
    title = driver.title

    return render(request, 'app/index.html', {
        'html': title
    })