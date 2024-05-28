from django.urls import path
from .views import get_all_blogs, get_blog_by_id, post_blog, update_blog
from . import views


urlpatterns = [
    path('blogs/', get_all_blogs, name='get_all_blogs'),
    path('blogs/<int:id>/', views.get_blog_by_id, name = 'get_blog_by_id'),
    path('blogs/create/', post_blog, name = 'post_blog'),
    path('blogs/update/<int:id>/', views.update_blog, name = 'update_blog'),
]