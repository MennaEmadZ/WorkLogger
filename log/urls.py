from django.urls import path
from . import views


urlpatterns = [
    path('add/', views.LogHoursView.as_view()),
    path('view/', views.logView.as_view(), name='logView')
]   