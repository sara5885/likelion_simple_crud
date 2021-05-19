from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog

# Create your views here.

def home(request):
    blog_objects=Blog.objects.all()
    return render(request, 'home.html',{'data':blog_objects})

def create_post(request):
    if request.method == 'POST':
        blog_object=Blog()
        blog_object.title=request.POST['title']
        blog_object.body=request.POST['body']
        blog_object.save()
        return redirect('/read_post/'+str(blog_object.id))
    return render(request,'create_post.html')

def read_post(request,id):
    blog_object = get_object_or_404(Blog, pk=id)
    return render(request,'read_post.html',{'data':blog_object})