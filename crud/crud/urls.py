
from django.contrib import admin
from django.urls import path, include
import viewcrud.urls
import viewcrud.views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', viewcrud.views.welcome, name='welcome'),
    path('funccrud/', include(viewcrud.urls)),
]
