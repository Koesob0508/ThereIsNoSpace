from django.urls import path
from . import views

app_name = 'nomad'
urlpatterns = [
    # /nomad/
    path('', views.IndexView.as_view(), name='index'),
    
    # /nomad/region
    path('region/', views.RegionList.as_view(), name='region'),

    # /nomad/coworking
    path('coworking/', views.CoworkingList.as_view(), name='coworking'),

    # /nomad/accommodation
    path('accommodation', views.AccommodationList.as_view(), name='accommodation'),
    
    # /nomad/region/99
    path('region/<int:pk>/', views.RegionDetail.as_view(), name='region_detail'),

    # /nomad/coworking/99
    path('coworking/<int:pk>/', views.CoworkingDetail.as_view(), name='coworking_detail'),

    # /nomad/accommodation/99
    path('accommodation/<int:pk>/', views.AccommodationDetail.as_view(), name='accommodation_detail'),
]