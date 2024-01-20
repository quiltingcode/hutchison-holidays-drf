from django.urls import path
from bookings import views

urlpatterns = [
    path('bookings/', views.BookingList.as_view()),
    path('booking/<int:pk>/', views.BookingDetail.as_view()),
]