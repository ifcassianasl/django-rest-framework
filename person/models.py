from django.db import models
import uuid


class Person(models.Model):
    name = models.CharField(max_length=100)
    born_date = models.DateField()

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name
