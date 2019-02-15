from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from api.models import Itinerary
from api.serializers import ItinerarySerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'itineraries': reverse('itineraries', request=request, format=format),
    })

class ItineraryViewSet(viewsets.ModelViewSet):
    queryset = Itinerary.objects.all()
    serializer_class = ItinerarySerializer