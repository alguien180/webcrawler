from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Link
from django.http import HttpResponseRedirect

def scrape(request):
    if request.method=="POST":
        site = request.POST.get('site','')
        page = requests.get(site)
        soup = BeautifulSoup(page.text, 'html.parser')

        for a_tag in soup.find_all('a'):
            link_address = a_tag.get('href')
            link_text = a_tag.string
            if link_address:  # avoid saving None
                Link.objects.create(address=link_address, name=link_text)
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()
    return render(request, 'scrapperapp/result.html', {'links': data})

def clear(request):
    Link.objects.all().delete()
    return render (request,'scrapperapp/result.html')