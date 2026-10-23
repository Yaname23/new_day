from django.contrib import admin
from django.urls import path
from .views import my_index

app_name = 'myapp'

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", my_index, name='index'),
]