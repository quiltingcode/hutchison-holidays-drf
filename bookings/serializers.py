from rest_framework import serializers
from .models import Booking


class BookingSerializer(serializers.ModelSerializer):
    """
    Serializer for the Profile model
    """
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(
        source='owner.profile.profile_pic.url'
    )

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner


    class Meta:
        model = Booking
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'booking_start_date',
            'booking_end_date', 'length_of_stay', 'notes', 'guests', 'cost',
            'paid', 'is_owner', 'profile_id', 'profile_image',

        ]