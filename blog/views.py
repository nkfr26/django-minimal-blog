from django.shortcuts import render

from .models import Post

# Create your views here.
def index(request):
    return render(request, "index.html", {
        "posts": Post.objects.order_by("id")
    })

def detail(request, slug):
    return render(request, "detail.html", {
        "post": Post.objects.get(slug=slug)
    })
