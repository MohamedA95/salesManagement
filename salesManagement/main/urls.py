from django.urls import path, include
from . import views
urlpatterns = [
    path('addpro', views.addpro),
    path('rmit', views.rmit),
    path('addit', views.addit),
    path('rep/sales', views.repsales),
    path('rep/products', views.repproducts),
    path('rep/batches', views.repbatches),
    path('home', views.home),
    path('',views.login)
]