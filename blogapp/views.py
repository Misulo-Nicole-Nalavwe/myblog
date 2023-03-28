from django.shortcuts import render
from django.http import HttpResponse
from blogappposts.models import Post

# Create your views here.
def frontpage(request):
    posts = Post.objects.filter(status=Post.ACTIVE)

    return render(request, 'blogapp/frontpage.html', {'posts':posts})

def about(request):
    return render(request, 'blogapp/about.html')

def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/" 
    ]
    return HttpResponse("\n".join(text), content_type = "text/plain")

