from django.urls import path

from . import views

urlpatterns = [
    path('listing/', views.listing, name='listing'),
    path('breadcrumb/', views.breadcrumb, name='breadcrumb'),
    path('location/', views.location, name='location'),
    path('type/', views.type, name='type'),
    path('purpose/', views.purpose, name='purpose'),
    path('popularProperties/', views.popularProperties, name='popularProperties'),
    # path('', views.index, name='index'),
]