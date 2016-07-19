from django.contrib.gis import admin

from playgrounds.models import Playground

class PlaygroundAdmin(admin.OSMGeoAdmin):
    default_lon = -8366872.286994299
    default_lat = 4859906.22026679
    default_zoom = 13

admin.site.register(Playground, PlaygroundAdmin)

