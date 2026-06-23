from django.urls import reverse_lazy
from .models import Post, Author
from .forms import PostForm,UserRegistrationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin


from django.shortcuts import redirect, render

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    TemplateView
)


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


class PostCreateView(LoginRequiredMixin,CreateView):

    model = Post

    form_class = PostForm

    template_name = "blog/post_form.html"

    success_url = reverse_lazy(
        "core:post_list"
    )

class PostUpdateView(LoginRequiredMixin,UpdateView):

    model = Post

    form_class = PostForm

    template_name = "blog/post_form.html"

    success_url = reverse_lazy(
        "core:post_list"
    )

class PostDeleteView(LoginRequiredMixin,DeleteView):

    model = Post

    template_name = "blog/post_confirm_delete.html"

    success_url = reverse_lazy(
        "core:post_list"
    )

class HomeView(TemplateView):
    template_name = "home.html"



def buscar_autores(request):
    query = request.GET.get("q", "")

    resultados = Author.objects.filter(name__icontains=query) if query else []

    return render(request, "blog/search_authors.html", {
        "resultados": resultados,
        "query": query
    })

from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class UserRegisterView(CreateView):

    model = User

    form_class = UserRegistrationForm

    template_name = "registration/register.html"

    success_url = reverse_lazy("core:login")

    def form_valid(self, form):

        self.object = form.save(commit=False)

        self.object.set_password(
            form.cleaned_data["password"]
        )

        self.object.save()

        return redirect("core:login")
    
class UserLoginView(LoginView):

    template_name = "registration/login.html"

    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    pass