from django.shortcuts import render, get_object_or_404
from .models import Blogger

def all_blogs(request):
    #limits the no of blog to 5
    #Blog = Blogger.objects.order_by('-date')[:5]
    Blog_object = Blogger.objects.all()
    return render(request, "blog/all_blogs.html", {"Blogs" : Blog_object})

def detail(request, blog_id):
    selected_blog = get_object_or_404(Blogger, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog':selected_blog})
