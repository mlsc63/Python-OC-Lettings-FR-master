from django.contrib import admin
from django.urls import path, include

from . import views

def trigger_error(request):
    division_by_zero = 1 / 0

urlpatterns = [
    #path('sentry-debug/', trigger_error),
    path('', views.index, name='index'),
    path('admin/', admin.site.urls),
    path('', include('letting.urls')),
    path('', include('profiles.urls'))
]
