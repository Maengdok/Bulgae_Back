from rest_framework import serializers
from english.models import English


class EnglishSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    label = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return English.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.label = validated_data.get('label', instance.label)
        return instance
