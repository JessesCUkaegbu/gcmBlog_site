from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path('category_list/', views.category_list, name="category_list"),
    path('post/', views.post, name="post"),
    path('post_detail/', views.post_detail, name="post_detail"),
    path('signUp/', views.signUp, name='signup'),
    path('login/', views.login, name='login'),
    path('category_detail/<int:category_id>/', views.category_detail, name="category_detail"),
]
