from django.shortcuts import render
from django.http import HttpResponse

import feedparser

def index(request):
    if request.GET.get('url'):
        url = request.GET['url']
        feed = feedparser.parse(url)
    else:
        feed = None
        
    return render(request, template_name='rss/index.html', context={'feed': feed})
    