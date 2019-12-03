from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('abaout',views.abaout, name='abaout'),
    path('store',views.store, name='store'),
]