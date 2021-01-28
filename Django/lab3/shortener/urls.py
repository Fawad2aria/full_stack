from django.urls import path
from . import views

app_name = 'shortener'
urlpatterns = [
    path('<str:shortcode>/', views.redirect_url, name='redirect_url'),
]