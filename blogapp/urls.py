from django.urls import path
from .views import get_all_blogs, get_blog_by_id, post_blog, update_blog

urlpatterns = [
    path('blogs/', get_all_blogs, name='get_all_blogs'),
    path('blogs/<int:pk>/', get_blog_by_id, name = 'get_blog_by_id'),
    path('blogs/create/', post_blog, name = 'post_blog'),
    path('blogs/update/<int:pk>/', update_blog, name = 'update_blog'),
]