# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from .models import Post, comentario
from django.utils import timezone
# Create your views here.
def post_list(request):
    posts_publicados = Post.objects.filter(data_publicacao__lte=timezone.now()).order_by('data_publicacao')
    return render(request, 'post_list.html', {'posts': posts_publicados})
def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    comentarios = comentario.objects.filter(post=post)
    return render (request, 'post_detail.html', {'post':post, 'comentarios': comentarios})