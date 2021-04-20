from django.shortcuts import render

from posts.models import Post


def index(request):
    context = {'title': 'Clean Blog', 'posts': Post.objects.all()}
    return render(request, 'posts/index.html', context)


def post(request, id):
    post = Post.objects.get(id=id)
    context = {'title': f'Clean Blog - {post.title}', 'post': post}
    return render(request, 'posts/post.html', context)
