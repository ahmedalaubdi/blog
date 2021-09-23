from django.urls import path
from . import views
urlpatterns = [
    path('', views.welcome),
    path('products/', views.index)
]