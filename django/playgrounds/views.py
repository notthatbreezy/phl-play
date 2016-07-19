from django.contrib.gis.geos import Point
from django.core.serializers import serialize
from django.http import HttpResponse

from .models import Playground

def playground(request):
    """Handle GET Requests for Playgrounds"""
    
    distance = request.GET.get('distance', None)
    lat = request.GET.get('lat', None)
    lng = request.GET.get('lng', None)

    if not all([distance, lat, lng]):
        playgrounds = Playground.objects.all()
    else:
        point = Point(float(lng), float(lat), srid=4326)
        point.transform(26918)
        circle = point.buffer(float(distance))
        playgrounds = Playground.objects.filter(location__within=circle)
    serialized = serialize('geojson', playgrounds, geometry_field='location', fields=('name', 'address'))
    return HttpResponse(serialized, content_type="application/json")

