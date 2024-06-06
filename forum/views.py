from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """
    View for a post list
    """
    queryset = Post.objects.all()
    template_name = "forum/index.html"
    paginate_by = 5


def post_detail(request, slug):
    """
    Display an individual post
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)

    return render(
        request,
        "forum/post_detail.html",
        {"post": post},
    )