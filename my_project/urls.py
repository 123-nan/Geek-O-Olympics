from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the URL patterns from the my_app.urls module
    path('', include('my_app.urls')),
]
from django.contrib import admin
from django.urls import path, include 

urlpatterns = [
    path('admin/', admin.site.urls),
    # Include the URL patterns from the my_app.urls module
    path('', include('my_app.urls')),
]
