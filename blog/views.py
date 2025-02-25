from django.shortcuts import render
from .models import Post

def post_list(request):
    posts = Post.objects.all()  # Получаем все записи
    return render(request, 'blog/post_list.html', {'posts': posts})
