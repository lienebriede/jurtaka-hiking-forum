from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    """
    View for a post list
    """
    queryset = Post.objects.all()
    template_name = "post_list.html"


