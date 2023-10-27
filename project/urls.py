from django.contrib import admin
from django.urls import path, include
from hello_world import views 


urlpatterns = [
    path('admin/', admin.site.urls),
     path('hello/', include('hello_world.urls')),
]

