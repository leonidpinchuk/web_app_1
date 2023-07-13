from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('comment', views.comment, name='comment'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('about-us', views.about, name='about')
]