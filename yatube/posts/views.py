from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    template = "posts/index.html"
    number_of_posts = 10
    posts = Post.objects.all()[:number_of_posts]
    context = {
        "posts": posts,
    }

    return render(request, template, context)


def group_posts(request, slug):
    number_of_posts = 10
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).all()[:number_of_posts]
    context = {
        "group": group,
        "posts": posts,
    }
    return render(request, "posts/group_list.html", context)
