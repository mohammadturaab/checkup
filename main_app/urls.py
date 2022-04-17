from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('findgame/', views.FindGame.as_view(), name="findgame"),
    path('creategame/', views.CreateGame.as_view(), name="creategame"),
    path('findgame/<int:pk>/', views.GameDetail.as_view(),name="gamedetail"),
    path('findgame/<int:pk>/update', views.GameUpdate.as_view(),name="gameupdate"),
    #LOGIN URLS
    path('accounts/signup/', views.signup_view, name="signup"),
    path('user/<username>/', views.profile, name='profile'),
]