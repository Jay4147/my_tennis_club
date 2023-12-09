from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('members/', views.members, name='members'),
    path('members/details/<int:id>', views.details, name='details'),
    path('testing/', views.testing, name='testing'),
    path('court/',views.court, name = "court"),
    path('court/court_details/<int:id>', views.court_detail, name='court_detail'),
]