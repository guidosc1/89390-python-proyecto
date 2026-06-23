from django.urls import path

from .views import (
    HomeView,
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView,
    buscar_autores,
    UserRegisterView,
    UserLoginView,
    UserLogoutView,
)

app_name = "core"

urlpatterns = [

    path(
        "",
        PostListView.as_view(),
        name="post_list"
    ),

    path(
        "<int:pk>/",
        PostDetailView.as_view(),
        name="post_detail"
    ),

    path(
        "create/",
        PostCreateView.as_view(),
        name="post_create"
    ),

    path(
        "<int:pk>/update/",
        PostUpdateView.as_view(),
        name="post_update"
    ),

    path(
        "<int:pk>/delete/",
        PostDeleteView.as_view(),
        name="post_delete"
    ),
    path(
    "",
    HomeView.as_view(),
    name="home"
    ),
    path(
    "buscar/",
    buscar_autores, 
    name="search_authors"
    ),
    path(
    "register/",
    UserRegisterView.as_view(),
    name="register"
    ),

    path(
        "login/",
        UserLoginView.as_view(),
        name="login"
    ),

    path(
        "logout/",
        UserLogoutView.as_view(),
        name="logout"
    ),
]