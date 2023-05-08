from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from category.models import Category
from post.models import Post

def home_view(request, category_slug = None):
    categories = None
    posts = None
    
    if category_slug != None:
        categories = get_object_or_404(Category,slug = category_slug)
        posts = Post.objects.all().order_by('-date_posted').filter(post_category = categories)
        posts_count = posts.count()
        context = {
        'news':posts,
        'count' : posts_count,
        }
        return render(request, 'home.html', context)
        
    else:
        posts = Post.objects.all()
        context = {
        'news':posts,
        }
    return render(request, 'home.html', context)
