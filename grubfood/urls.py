from django.contrib import admin

from django.urls import include, path

urlpatterns = [
    path('webkiosk/', include('webkiosk.urls')),
    path('admin/', admin.site.urls),
]
