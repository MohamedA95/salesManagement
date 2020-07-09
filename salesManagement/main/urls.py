from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('addpro', views.add_product),
    path('rmit', views.remove_item),
    path('addit', views.add_item),
    path('rep/sales', views.report_sales),
    path('rep/products', views.report_products),
    path('rep/batches', views.report_batches),
    path('rep/statistics/',views.report_statistics),
    path('app/rmsaleorder',views.remove_sales_order),
    path('home', views.home),
    path('calc',views.calculate_profit),
    path('',views.login),
    path('ajax/productbatches/<str:product>/',views.get_batches_for_product)

    
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)