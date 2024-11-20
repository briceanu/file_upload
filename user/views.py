from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from rest_framework.parsers import MultiPartParser, FormParser



class CreateListAPI(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = [MultiPartParser,FormParser]

 