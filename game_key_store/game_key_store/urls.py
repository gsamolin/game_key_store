from django.urls import include, path
from django.contrib import admin

urlpatterns = [
    path('store/', include('store.urls')),  # Подключение маршрутов приложения store
    path('admin/', admin.site.urls),
    path('api/', include('store.urls')),
]
