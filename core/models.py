from django.db import models
from django.core.exceptions import ValidationError


class Author(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(auto_now_add=True)

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE
    )

    tags = models.ManyToManyField(
        Tag
    )

    # 1. Agregamos el campo para la imagen de portada aquí:
    imagen_portada = models.ImageField(upload_to='portadas/', null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-published_date']

    def clean(self):
        if len(self.title) < 5:
            raise ValidationError(
                {'title': 'El título debe tener al menos 5 caracteres.'}
            )