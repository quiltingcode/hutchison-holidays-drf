from django.urls import path
from bookings import views

urlpatterns = [
    path('bookings/', views.BookingList.as_view()),
    path('bookings/<int:pk>/', views.BookingDetail.as_view()),
]