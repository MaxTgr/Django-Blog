from django.shortcuts import render
from django.http import HttpResponse

from .models import Posts

def index(request):

    posts = Posts.objects.all()[:10]

    context = {
        'posts': posts
    }

    return render(request, 'posts/index.html', context) 
