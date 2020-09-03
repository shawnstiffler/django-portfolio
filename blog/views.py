from django.shortcuts import render
from .models import Blogger

def all_blogs(request):
    #limits the no of blog to 5
    #Blog = Blogger.objects.order_by('-date')[:5]
    Blog = Blogger.objects.all()
    return render(request, "blog/all_blogs.html", {"Blogs" : Blog})
