from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('insert/', insert),
    path('delete/', delete),
    path('update/', update)
]