from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User  # Add this import statement
from .forms import PostForm, ImageForm, CommentForm, CategoryForm, SubcategoryForm
from .models import Post, Image, Comment, Category, SubCategory


#######################################
def create_post(request):
    if request.method == "POST":
        post_form = PostForm(request.POST)
        image_form = ImageForm(request.POST, request.FILES)
        if post_form.is_valid() and image_form.is_valid():
            post = post_form.save(commit=False)
            post.created_by = request.user
            post.save()
            images = request.FILES.getlist("image")
            for image in images:
                Image.objects.create(post=post, image=image)
            return redirect(
                "RV_vpost_list"
            )  # Redirect to a list of posts or another page
    else:
        post_form = PostForm()
        image_form = ImageForm()
    return render(
        request,
        "blog/create_post.html",
        {"post_form": post_form, "image_form": image_form},
    )


def update_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post_form = PostForm(request.POST, instance=post)
        image_form = ImageForm(request.POST, request.FILES)
        if post_form.is_valid() and image_form.is_valid():
            post = post_form.save(commit=False)
            post.save()
            images = request.FILES.getlist("image")
            for image in images:
                Image.objects.create(post=post, image=image)
            return redirect(
                "RV_vpost_list"
            )  # Redirect to a list of posts or another page
    else:
        post_form = PostForm(instance=post)
        image_form = ImageForm()
    return render(
        request,
        "blog/update_post.html",
        {"post_form": post_form, "image_form": image_form},
    )


def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        post.delete()
        return redirect("RV_vpost_list")  # Redirect to a list of posts or another page
    return render(request, "blog/delete_post.html", {"post": post})


def post_list(request):
    posts = Post.objects.all()
    return render(request, "blog/post_list.html", {"posts": posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    if request.method == "POST":
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect("RV_vpost_detail", post_id=post.id)
    else:
        comment_form = CommentForm()
    return render(
        request, "blog/post_detail.html", {"post": post, "comment_form": comment_form}
    )


###
def category_list(request):
    categories = Category.objects.all()
    return render(request, "blog/category_list.html", {"categories": categories})


def create_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("RV_vcategory_list")
    else:
        form = CategoryForm()
    return render(request, "blog/create_category.html", {"form": form})


def update_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect("RV_vcategory_list")
    else:
        form = CategoryForm(instance=category)
    return render(request, "blog/update_category.html", {"form": form})


def category_delete(request, pk):
    category = get_object_or_404(Category, pk=pk)
    if request.method == "POST":
        category.delete()
        return redirect("category_list")
    return render(request, "blog/delete_category.html", {"category": category})


"""
def subcategory_list(request):
    subcategories = SubCategory.objects.all()
    return render(request, "blog/category_list.html", {"subcategories": subcategories})
"""

"""
def create_subcategory(request):
    if request.method == "POST":
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("subcategory_list")
    else:
        form = SubcategoryForm()
    return render(request, "blog/create_subcategory.html", {"form": form})



def update_subcategory(request, subcategory_id):
    subcategory = get_object_or_404(SubCategory, id=subcategory_id)
    if request.method == "POST":
        form = SubcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect("RV_vsubcategory_list")
    else:
        form = SubcategoryForm(instance=subcategory)
    return render(request, "blog/update_subcategory.html", {"form": form})

"""


# Subcategorías
def subcategory_list(request):
    subcategories = SubCategory.objects.all()
    return render(
        request, "blog/subcategory_list.html", {"subcategories": subcategories}
    )


def subcategory_create(request):
    if request.method == "POST":
        form = SubcategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("RV_vsubcategory_list")
    else:
        form = SubcategoryForm()
    return render(request, "blog/create_subcategory.html", {"form": form})


def subcategory_edit(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    if request.method == "POST":
        form = SubcategoryForm(request.POST, instance=subcategory)
        if form.is_valid():
            form.save()
            return redirect("RV_vsubcategory_list")
    else:
        form = SubcategoryForm(instance=subcategory)
    return render(request, "blog/update_subcategory.html", {"form": form})


def subcategory_delete(request, pk):
    subcategory = get_object_or_404(SubCategory, pk=pk)
    if request.method == "POST":
        subcategory.delete()
        return redirect("subcategory_list")
    return render(request, "blog/delete_subcategory.html", {"subcategory": subcategory})
