from rest_framework import serializers
from english.models import English


class EnglishSerializer(serializers.ModelSerializer):
    class Meta:
        model = English
        fields = "__all__"

    def create(self, validated_data):
        return English.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.label = validated_data.get('label', instance.label)
        instance.save()
        return instance
