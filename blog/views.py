from django.shortcuts import render, get_object_or_404
from .models import Blog


def allblogs(reqest):
    blogs = Blog.objects
    return render(reqest, 'blog/allblogs.html', {'blogs': blogs})  # Адрес файла allblogs.html


def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'blog': detail_blog})
