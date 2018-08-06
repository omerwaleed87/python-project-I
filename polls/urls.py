from django.urls import path

from . import views

urlpatterns = [
    path('listing/', views.listing, name='listing'),
    path('breadcrumb/', views.breadcrumb, name='breadcrumb'),
    # path('', views.index, name='index'),
]