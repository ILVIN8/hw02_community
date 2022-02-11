from django.shortcuts import render, get_object_or_404

from .models import Post, Group

number_of_posts = 10


def index(request):
    template = "posts/index.html"
    posts = Post.objects.all()[:number_of_posts]
    context = {
        "posts": posts,
    }

    return render(request, template, context)


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:number_of_posts]
    context = {
        "group": group,
        "posts": posts,
    }
    return render(request, "posts/group_list.html", context)
