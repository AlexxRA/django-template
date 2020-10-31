from rest_framework import viewsets
from .serializers import *


# Create your views here.
class StudentViewSet(viewsets.ModelViewSet):
    """
    API Endpoint [get, post, put, delete, get(id), patch]
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
