from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^menu/nueva/$', views.menu_nuevo, name='menu_nuevo'),
    ]
