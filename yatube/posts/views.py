from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    template = "posts/index.html"
    number_of_posts = 10
    posts = Post.objects.order_by("-pub_date")[:number_of_posts]
    context = {
        "posts": posts,
    }

    class Meta:
        verbose_name = "Пост"
        verbose_plural_name = "Посты"
        ordering = ["-pub_date"]

    return render(request, template, context)


def group_posts(request, slug):
    number_of_posts = 10
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by("-pub_date")[
        :number_of_posts
    ]
    context = {
        "group": group,
        "posts": posts,
    }
    return render(request, "posts/group_list.html", context)
