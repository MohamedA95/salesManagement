"""salesManagement URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.i18n import i18n_patterns
from main.viewset import feeprogViewSet,productViewSet,batchViewSet,salesViewSet, statisticsViewset,salesCustom
from main.views import changeBatchStatus,editCompanyCapital
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'feeprogVS',feeprogViewSet)
router.register(r'productVS',productViewSet)
router.register(r'batchVS',batchViewSet)
router.register(r'salesVS',salesViewSet)
router.register(r'statisticsVS',statisticsViewset)

urlpatterns = [
    path('i18n/', include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('api/salescustom/<str:orderid>/',salesCustom.as_view()),
    path('api/changeBatchStatus/',changeBatchStatus),
    path('api/editCompanyCapital/',editCompanyCapital),
    path('api/',include(router.urls)),
]

urlpatterns += i18n_patterns(
    path('',include('main.urls')),
    path('app/',include('main.urls')))