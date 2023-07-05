from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    #create
    path('signup/', views.signup, name='signup'),
    
    #update
    path('edit/', views.edit, name='edit'),

    #create
    path('login/', views.login, name='login'),
    
    #delete
    path('logout/', views.logout, name='logout'),
    
    #read
    path('<str:username>/', views.profile, name='profile'),

    #create
    path('<int:id>/following/', views.following, name='following'),

]