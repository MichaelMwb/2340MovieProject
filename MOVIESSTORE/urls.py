from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Assuming you have a home app
   # path('about/', include('home.urls')),  # Assuming you have a home app
    path('movies/', include('movies.urls')),
    path('accounts/', include('accounts.urls')),  # Assuming you have an accounts app
    path('cart/', include('cart.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)