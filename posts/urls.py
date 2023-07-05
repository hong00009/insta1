from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name = 'posts'

urlpatterns = [
    #read
    path('', views.index, name='index'),
    #create
    path('create/', views.create, name='create'),
    #delete
    path('<int:id>/delete/', views.delete, name='delete'),

    #create
    path('<int:id>/comments/create', views.comments_create, name='comments_create'),
    
    path('<int:id>/likes/', views.likes, name='likes'),
] 