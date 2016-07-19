from __future__ import unicode_literals

from django.contrib.gis.db import models


class Playground(models.Model):
    """Location with swings, slides, and other playground essentials"""

    def __str__(self):
        return self.name
    
    location = models.PointField(srid=26918)
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    address = models.TextField()
