from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('', views.index, name='account_index'),
    path('<int:user_pk>/', views.user_detail, name='account_user_detail'),
    path('signup/', views.signup, name='account_signup'),
    path('login/', views.login, name='account_login'),
    path('logout/', views.logout, name='account_logout'),
    path('<int:user_pk>/follow/', views.follow, name='follow'),
]