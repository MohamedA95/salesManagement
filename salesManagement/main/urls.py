from django.urls import path, include
from . import views
from .viewset import feeprogViewSet,productViewSet,batchViewSet,salesViewSet,salesCustom
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router=routers.DefaultRouter()
router.register(r'feeprogVS',feeprogViewSet)
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
    path('api/salescustom/<str:orderid>/',salesCustom.as_view()),
    path('api/',include(router.urls)),
    path('ajax/productbatches/<str:product>/',views.getBatchesForProduct)

    
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)