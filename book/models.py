from django.db import models
from person.models import Person
import uuid


class Book(models.Model):
    title = models.CharField(max_length=200)
    pages = models.IntegerField()
    author = models.ForeignKey(Person, on_delete=models.CASCADE)

    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    class Meta:
        db_table = 'book'

    def __str__(self):
        return self.title
