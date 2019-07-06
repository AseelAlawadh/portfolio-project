from django.shortcuts import render, get_object_or_404
from .models import MyBlog
# Create your views here.
def allblogs(request):
    blogs = MyBlog.objects
    return render(request, 'myblog/allblogs.html',{'blogs':blogs})

def detail(request, blog_id):
    detailblog = get_object_or_404(MyBlog, pk=blog_id) #pk it's primary key
    return render(request, 'myblog/detail.html', {'blog':detailblog})