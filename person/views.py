from rest_framework import viewsets
from .models import Person
from .serializers import PersonSerializer


class PersonView(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

