from django.urls import path, include
from . import views
urlpatterns = [
    path('addpro', views.addpro),
    path('rmit', views.rmit),
    path('addit', views.addit),
    path('rep', views.rep),
    path('home', views.home),
    path('',views.login)
]