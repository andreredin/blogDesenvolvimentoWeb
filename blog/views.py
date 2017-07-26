# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Post, comentario
from django.utils import timezone
from .forms import formComentario, formPost


# Create your views here.
def post_list(request):

    posts_publicados = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    return render(request, 'post_list.html', {'posts': posts_publicados})

def post_detail(request, pk):

    if request.method == "POST":
        form =  formComentario(request.POST)
        if form.is_valid():
            Comentario = form.save(commit=False)
            Comentario.autor = request.user
            Comentario.data = timezone.now()
            Comentario.post = Post.objects.get(id=pk)
            Comentario.save()
            return redirect(post_detail, pk=pk)
    else:
        post = Post.objects.get(id=pk)
        comentarios = comentario.objects.filter(post=post).order_by('data')
        form = formComentario()


    return render(request, 'post_detail.html', {'post': post, 'comentarios': comentarios, 'form': form})

def post_new(request):

    if request.method == "POST":
        form =  formPost(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.data_criacao = timezone.now()
            post.save()
            form = formPost()
            return render(request, 'post_new.html', {'form': form})

    else:
        form = formPost()
        return render(request, 'post_new.html', {'form': form})