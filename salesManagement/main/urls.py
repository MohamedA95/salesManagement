from django.urls import path,include
from . import views
from django.contrib.auth import views as auth_vi
urlpatterns = [
    path('addpro', views.addpro),
    path('rmit', views.rmit),
path('addit', views.addit),
path('rep', views.rep),
path('', auth_vi.LoginView.as_view(template_name='login.html')),
path('home',views.home)


]