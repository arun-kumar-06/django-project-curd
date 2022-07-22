from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.http import HttpResponse
from django.contrib import messages
from .models import Posts
from .serializers import *
from rest_framework.views import APIView
def index(request):
    posts = Posts.objects.all()
    return render(request, 'index.html', {
        'posts': posts
    })

def create(request):
    if request.POST:
        try:
            req = request.POST
            postser=PostSerializer(
                data={"title":req.get('title'),
                "content":req.get('content'),
                "slug":slugify(req.get('title'))
            })
            if postser.is_valid(raise_exception=True):
                postser.save()
            messages.success(request, 'The record was saved successfully')
            return redirect('/')
        except Exception as e: 
            messages.error(request, 'title can not be empty')
            return redirect('/')
    else:
        return render(request, 'create.html')

def update(request, post_id):
    if request.POST:
        try:
            req = request.POST
            post = Posts.objects.get(id=post_id)
            postser=PostSerializer(
                post,data={"title":req.get('title'),
                "content":req.get('content'),
                "slug":slugify(req.get('title'))
            })
            if postser.is_valid(raise_exception=True):
                postser.save()
            messages.success(request, 'The record was saved successfully')
            return redirect('/')
        except Exception as e: 
            messages.error(request, 'title can not be empty')
            return redirect('/')

    else:
        post = Posts.objects.get(id=post_id)
        return render(request, 'update.html', {
            'id': post.id,
            'title': post.title,
            'slug': post.slug,
            'content': post.content
        })

def read(request, post_slug):
    post = Posts.objects.get(slug=post_slug)
    return render(request, 'detail.html', {
        'id': post.id,
        'title': post.title,
        'slug': post.slug,
        'content': post.content
    })

def delete(request, post_id):
    post = Posts.objects.get(id=post_id)
    post.delete()
    messages.success(request, 'The record was deleted successfully')
    return redirect('/')


class PostListView(APIView):
    def get(self,request):
        posts = Posts.objects.all()
        return render(request, 'index.html', {
            'posts': posts
        })


class PostCreateView(APIView):
    def get(self,request):
        return render(request, 'create.html')
    def post(self,request):
        req = request.POST
        post = Posts(title=req.get('title'), slug=slugify(req.get('title')), content=req.get('content'))
        post.save()
        messages.success(request, 'The record was saved successfully')
        return redirect('/')

class PostUpdateView(APIView):
    def get(self,request,post_id):
        post = Posts.objects.get(id=post_id)
        return render(request, 'update.html', {
            'id': post.id,
            'title': post.title,
            'slug': post.slug,
            'content': post.content
        })
    def post(self,request,post_id):
        req = request.POST
        post = Posts.objects.get(id=post_id)
        post.title = req.get('title')
        post.slug = slugify(req.get('title'))
        post.content = req.get('content')
        post.save()
        messages.success(request, 'The record was saved successfully')
        return redirect('/')

class PostDeleteView(APIView):
    def get(self,request,post_id):
        post = Posts.objects.get(id=post_id)
        post.delete()
        messages.success(request, 'The record was deleted successfully')
        return redirect('/')

class PostDetailView(APIView):
    def get(self,request,post_slug):
        post = Posts.objects.get(slug=post_slug)
        return render(request, 'detail.html', {
            'id': post.id,
            'title': post.title,
            'slug': post.slug,
            'content': post.content
        })

