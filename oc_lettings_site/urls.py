from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('letting.urls')),
    path('', include('profiles.urls')),
    path('', include('app.urls'))
]
