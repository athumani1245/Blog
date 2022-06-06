from .models import Category
from post.models import Post

def menu_links(request):
    links = Category.objects.all()
    return dict(links = links)

def latest_view(request):
    post = Post.objects.all().order_by('-date_posted')
    return dict(post = post)