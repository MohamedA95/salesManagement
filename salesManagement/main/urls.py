from django.urls import path, include
from . import views
from .viewset import commissionViewSet,productViewSet,batchViewSet,salesViewSet
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router=routers.DefaultRouter()
router.register(r'commissionVS',commissionViewSet)
router.register(r'productVS',productViewSet)
router.register(r'batchVS',batchViewSet)
router.register(r'salesVS',salesViewSet)

urlpatterns = [
    path('addpro', views.addpro),
    path('rmit', views.rmit),
    path('addit', views.addit),
    path('rep/sales', views.repsales),
    path('rep/products', views.repproducts),
    path('rep/batches', views.repbatches),
    path('home', views.home),
    path('calc',views.calc),
    path('',views.login),
    path('api/',include(router.urls)),
    
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)