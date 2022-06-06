from unicodedata import category
from django.shortcuts import render
from .models import Post
from category.models import Category

# Create your views here.
#single post view

def post_detail(request, category_slug, post_slug):
    try:
        post_details = Post.objects.get(post_category__slug = category_slug, slug = post_slug)
    except Exception as e:
        raise e
    context = {
        'post_detail': post_details,
    }
    return render(request, 'post_details.html', context)
