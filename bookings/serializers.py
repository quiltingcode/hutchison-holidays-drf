from rest_framework import serializers
from .models import Booking
from django.contrib.humanize.templatetags.humanize import naturaltime

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
    created_at = serializers.SerializerMethodField()
    updated_at = serializers.SerializerMethodField()


    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_created_at(self, obj):
        return naturaltime(obj.created_at)

    def get_updated_at(self, obj):
        return naturaltime(obj.updated_at)
    class Meta:
        model = Booking
        fields = [
            'id', 'owner', 'created_at', 'updated_at', 'booking_start_date',
            'booking_end_date', 'length_of_stay', 'notes', 'guests', 'cost',
            'paid', 'is_owner', 'profile_id', 'profile_image',

        ]