from rest_framework import serializers
from korean.models import Korean


class KoreanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Korean
        fields = "__all__"

    def create(self, validated_data):
        return Korean.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.label = validated_data.get('label', instance.label)
        instance.save()
        return instance
