from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404

# Create your views here.
def post_list(request):
    blog_title = 'KameLabs blog'
    posts = Post.objects.order_by('published_date')
    return render(request, 'blog/post_list.html', 
        {'posts':posts, 'blog_title':blog_title})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})        