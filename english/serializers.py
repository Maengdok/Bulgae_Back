from rest_framework import serializers
from english.models import English


class EnglishSerializer(serializers.ModelSerializer):
    model = English
    fields = "__all__"
