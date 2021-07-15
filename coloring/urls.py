from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('demo', views.demo, name='demo'),
    path('new_interaction', views.index, name='new_interaction'),
    path('home', views.home, name='home'),
    path('artboard', views.artboard, name='artboard'),
    path('login', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('profile', views.profile, name='profile'),
    path('clashes', views.clashes, name='clashes'),
    path('leaderboard', views.leaderboard, name='leaderboard'),
]
