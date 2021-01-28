from django.db import models

class GroceryItem(models.Model):
    description = models.CharField(max_length=200)
    quantity = models.IntegerField(default=0)
    unit = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(null=True, blank=True)
    completed_date = models.DateTimeField(null=True, blank=True)
