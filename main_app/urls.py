from django.urls import path
from . import views


urlpatterns = [
    path('', views.Home.as_view(), name="home"),
    path('findgame/', views.FindGame.as_view(), name="findgame"),
    path('creategame/', views.CreateGame.as_view(), name="creategame"),
    path('findgame/<int:pk>/', views.GameDetail.as_view(),name="gamedetail"),
    path('findgame/<int:pk>/update', views.GameUpdate.as_view(),name="gameupdate"),
    path('findgame/<int:pk>/delete', views.GameDelete.as_view(),name="gamedelete"),
    #LOGIN URLS
    path('accounts/signup/', views.signup_view, name="signup"),
    path('user/<username>/', views.profile, name='profile'),
    #Group URLs
    path('<int:pk>/groupcreate/', views.CreateGroup.as_view(), name="groupcreate"),
    path('groupdetails/<int:group_id>', views.GroupDetails, name='groupdetails'),
    # path('groupjoin/<int:group_id>', views.GroupJoin.as_view(), name="groupjoin")
]