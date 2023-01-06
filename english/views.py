from rest_framework.generics import ListAPIView
from rest_framework.generics import CreateAPIView
from rest_framework.generics import DestroyAPIView
from rest_framework.generics import UpdateAPIView

from english.models import English
from english.serializers import EnglishSerializer


class ListEnglishAPIView(ListAPIView):
    queryset = English.objects.all()
    serializer = EnglishSerializer
