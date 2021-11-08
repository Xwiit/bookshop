from django.urls import path 
from . import views


urlpatterns =[
    path('', views.index, name='home-page'),
    path('detail/<str:pk>/', views.detail, name='detail-page')
]
