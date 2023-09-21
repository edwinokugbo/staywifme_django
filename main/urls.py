from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='home'),
    path('landing/', views.Landing.as_view(), name='landing'),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    # path('signup/', SignupPageView.as_view(), name="home"),
]
