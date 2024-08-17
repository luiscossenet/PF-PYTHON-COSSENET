from django.urls import path
from .views import *

urlpatterns = [
    # Blogs
    path("create/", create_post, name="RV_vcreate_post"),
    path("post", post_list, name="RV_vpost_list"),
    path("update/<int:post_id>/", update_post, name="RV_vupdate_post"),
    path("delete/<int:post_id>/", delete_post, name="RV_vdelete_post"),
    path("post/<int:post_id>/", post_detail, name="RV_vpost_detail"),
    # Categorias
    path("categories/", category_list, name="RV_vcategory_list"),
    path("categories/new/", create_category, name="RV_vcreate_category"),
    path(
        "categories/edit/<int:category_id>/", update_category, name="RV_vcategory_edit"
    ),
    path("categories/delete/<int:pk>/", category_delete, name="RV_vcategory_delete"),
    # Subcategorias
    path("subcategories/", subcategory_list, name="RV_vsubcategory_list"),
    path(
        "subcategories/new/",
        subcategory_create,
        name="RV_vsubcategory_create",
    ),
    path("subcategories/edit/<int:pk>/", subcategory_edit, name="RV_vsubcategory_edit"),
    path(
        "subcategories/delete/<int:pk>/",
        subcategory_delete,
        name="RV_vsubcategory_delete",
    ),
]
