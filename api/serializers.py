from rest_framework import serializers
from api.models import Itinerary

class ItinerarySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Itinerary
        fields = "__all__"