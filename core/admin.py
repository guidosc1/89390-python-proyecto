from django.contrib import admin
from .models import Author, Post, Tag


class PostInline(admin.TabularInline):
    model = Post
    extra = 1


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "email")
    search_fields = ("name", "email")
    inlines = [PostInline]



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "author",
        "published_date",
    )

    search_fields = (
        "title",
        "content",
    )

    list_filter = (
        "author",
        "published_date",
    )
    filter_horizontal = ("tags",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)

