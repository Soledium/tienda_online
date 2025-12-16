
from django.contrib import admin
from django.urls import path
from mainapp import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('tazones/', views.tazones, name='tazones'),
    path('poleras/', views.poleras, name='poleras'),
    path('polerones/', views.polerones, name='polerones'),
    path('zapatillas/', views.zapatillas, name='zapatillas'),
    path('solicitud/', views.solicitar, name='solicitud'),
    path('seguimiento', views.seguimiento, name='seguimiento'),
    path("api/", include("mainapp.api_urls")),
    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

