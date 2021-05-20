from django.shortcuts import render
from .models import Post


# Create your views here.

def index(request):
    posts = Post.objects.all()
    context = {
        'posts': posts
    }
    return render(request, 'blog/index.html', context)


def support(request):
    return render(request, 'blog/support_us.html')


def contact(request):
    return render(request, 'blog/contact.html')


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, "blog/post_detail.html", {'post': post})
