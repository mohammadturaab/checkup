from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('findgame/', views.FindGame.as_view(), name="findgame"),
    path('creategame/', views.CreateGame.as_view(), name="creategame"),
    path('findgame/<int:pk>/', views.GameDetail.as_view(), name="gamedetail"),
    #LOGIN URLS
    path('accounts/signup/', view.signup_view, name="signup"),
]