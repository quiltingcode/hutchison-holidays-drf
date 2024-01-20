from rest_framework import generics, permissions, filters
from .models import Booking
from .serializers import BookingSerializer
from hutch_hols.permissions import IsOwnerOrReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class BookingList(generics.ListCreateAPIView):
    """
    List bookings or create a booking if logged in
    The perform_create method associates the booking with the logged in user.
    """
    serializer_class = BookingSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly
    ]
    queryset = Booking.objects.all()
    filter_backends = [
        filters.OrderingFilter,
        filters.SearchFilter,
        DjangoFilterBackend,
    ]
    filterset_fields = {
        'owner__profile': ['exact'],
        'booking_start_date': ['lte'],
    }
    search_fields = [
        'owner__username',
    ]
    ordering_fields = [
        'booking_start_date'
    ]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class BookingDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a booking, or update or delete it by id if you own it.
    """
    serializer_class = BookingSerializer
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Booking.objects.all()
