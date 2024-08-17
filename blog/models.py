from django.db import models
from django.contrib.auth.models import User
import uuid
from AppMagico.models import Estado, Empresa  # Import Estado and Empresa from AppMagico


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, related_name="subcategories", on_delete=models.CASCADE
    )
    keywords = models.TextField()

    def __str__(self):
        return self.name


class Post(models.Model):
    TYPE_CHOICES = [
        ("image", "Image"),
        ("carousel", "Carousel"),
    ]
    title = models.CharField(max_length=200)
    resumen = models.TextField()
    content = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    post_type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    status = models.ForeignKey(Estado, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    subcategory = models.ForeignKey(SubCategory, on_delete=models.CASCADE)
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    post = models.ForeignKey(Post, related_name="images", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="images/")
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return str(self.unique_id)


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
