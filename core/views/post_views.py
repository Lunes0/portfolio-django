from django.views.generic import ListView, DetailView
from ..models import Post


class PostListView(ListView):
    model = Post
    template_name = "core/index.html"
    context_object_name = "posts"

    # def get_queryset(self):
    # return Post.objects.filter(status=1).order_order_by("-created_on")


class PostDetailView(DetailView):
    model = Post
    template_name = "core/detail.html"
    context_object_name = "post"
