from django.urls import reverse_lazy
from .models import Post
from .forms import PostForm

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)

from django.contrib.auth.mixins import LoginRequiredMixin

class PostListView(ListView):

    model = Post

    template_name = "blog/post_list.html"

    context_object_name = "posts"

    def get_queryset(self):

        return (
            Post.objects
            .filter(
                published_date__isnull=False
            )
            .order_by("-published_date")
        )
    
class PostDetailView(DetailView):

    model = Post

    template_name = "blog/post_detail.html"

    context_object_name = "post"


class PostCreateView(CreateView):

    model = Post

    form_class = PostForm

    template_name = "blog/post_form.html"

    success_url = reverse_lazy(
        "post_list"
    )

class PostUpdateView(UpdateView):

    model = Post

    form_class = PostForm

    template_name = "blog/post_form.html"

    success_url = reverse_lazy(
        "post_list"
    )

class PostDeleteView(LoginRequiredMixin,DeleteView):

    model = Post

    template_name = "blog/post_confirm_delete.html"

    success_url = reverse_lazy(
        "post_list"
    )