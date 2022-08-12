from django.urls import path

from . import views

urlpatterns = [
    path('login/', views.loginView),
    path('register/', views.registerView),
    path('logout/', views.logoutView),
]
