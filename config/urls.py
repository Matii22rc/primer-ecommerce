from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # Aquí incluiremos las URLs de nuestras apps más adelante
    path('', include('products.urls', namespace='products')),
    path('', include('cart.urls', namespace='cart'))
]

# Esto permite que Django sirva archivos de imagen durante el desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)