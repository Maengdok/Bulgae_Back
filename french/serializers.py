from rest_framework import serializers
from french.models import French


class FrenchSerializer(serializers.ModelSerializer):
    class Meta:
        model = French
        fields = "__all__"

    def create(self, validated_data):
        return French.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.label = validated_data.get('label', instance.label)
        instance.save()
        return instance
