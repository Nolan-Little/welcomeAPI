from django.db import models


class Itinerary(models.Model):
    name = models.CharField(max_length=50, null=True)
    park = models.CharField(max_length=50, null=True)
    restaurant = models.CharField(max_length=50, null=True)
    concert = models.CharField(max_length=50, null=True)
    meetup = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name
