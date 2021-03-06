from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, "foodblog/post_list.html", {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'foodblog/post_detail.html', {'post': post})

def recipe(request):
    return render(request, 'foodblog/recipe.html')

def contact(request):
    return render(request, 'foodblog/contact.html')