from django import forms
from .models import Post, Image, Comment, Category, SubCategory # Asegúrate de que tienes un modelo llamado UserProfile



class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
            "title",
            "resumen",
            "content",
            "start_date",
            "end_date",
            "post_type",
            "status",
            "category",
            "subcategory",
            "empresa",
        ]


class ImageForm(forms.ModelForm):
    class Meta:
        model = Image
        fields = ["image"]

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image:
            valid_mime_types = [
                "image/jpeg",
                "image/png",
                "image/gif",
                "image/tiff",
                "video/mp4",
                "application/pdf",
            ]
            if image.content_type not in valid_mime_types:
                raise forms.ValidationError("Unsupported file type.")
        return image


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["author", "text"]


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]


class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = SubCategory
        fields = ["name", "category"]
