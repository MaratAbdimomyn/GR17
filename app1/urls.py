from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('insert/', insert),
    path('delete/', delete),
    path('update/', update),
    path('search/', search),
]