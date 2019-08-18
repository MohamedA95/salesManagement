from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('addpro', views.addpro),
    path('rmit', views.rmit),
    path('addit', views.addit),
    path('rep/sales', views.repsales),
    path('rep/products', views.repproducts),
    path('rep/batches', views.repbatches),
    path('rep/statistics/',views.repstatistics),
    path('app/rmsaleorder',views.rmsaleorder),
    path('home', views.home),
    path('calc',views.calc),
    path('',views.login),
    path('ajax/productbatches/<str:product>/',views.getBatchesForProduct)

    
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)