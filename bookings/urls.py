from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('book/', views.book_appointment, name='book'), 
    path('book-appointment/', views.book_appointment, name='book_appointment'),
    path('confirmation/<int:booking_id>/', views.confirmation, name='confirmation'),
]