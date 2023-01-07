import json
from django.conf import settings

from rest_framework.decorators import api_view, schema, action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from drf_yasg.utils import swagger_auto_schema

from services.json_response import json_normalizer
from english.models import English
from .serializers import EnglishSerializer
from .schemas import get_english_schema, get_english_list_schema, add_english_schema, update_english_schema, \
    delete_english_schema


class EnglishViewSet(ViewSet):
    def __init__(self):
        self.status = settings.HTTP_CONSTANTS['SUCCESS']

    @swagger_auto_schema(methods=['GET'], tags=['English'], operation_description="Get english", responses=get_english_list_schema())
    @api_view(['GET'])
    def english_list(self):
        queryset = English.objects.all()
        serializer = EnglishSerializer(queryset, many=True)
        response = json_normalizer(data=serializer.data)
        return Response(response, status=self.status)

    @swagger_auto_schema(methods=['GET'], tags=['English'], operation_description="Get english", responses=get_english_schema())
    @api_view(['GET'])
    def get_english(self, english_id):
        try:
            queryset = English.objects.get(pk=english_id)
            serializer = EnglishSerializer(queryset)
            response = json_normalizer(data=serializer.data)
        except English.DoesNotExist:
            response = json_normalizer(code='NOT_FOUND', result='Not found', message='English not found.')
            self.status = settings.HTTP_CONSTANTS['NOT_FOUND']
        return Response(response, status=self.status)

    @swagger_auto_schema(
        methods=['POST'],
        tags=['English'],
        operation_description="Add english",
        responses=add_english_schema()
    )
    @api_view(['POST'])
    def add_english(self, request):
        decode = request.body.decode('utf-8')
        serializer = EnglishSerializer(data=decode)

        if not serializer.is_valid():
            response = json_normalizer(
                code='INTERNAL_SERVER_ERROR',
                result='Form is not valid.',
                message=serializer.errors
            )
            self.status = settings.HTTP_CONSTANTS['INTERNAL_SERVER_ERROR']
            return Response(response, status=self.status)

        serializer.save()
        response = json_normalizer(message='English created successfully.', data=serializer.data)
        return Response(response, status=self.status)

    @swagger_auto_schema(
        methods=['PUT'],
        tags=['English'],
        operation_description="Update english",
        responses=update_english_schema()
    )
    @api_view(['PUT'])
    def update_english(self, request):
        decode = request.body.decode('utf-8')
        content = json.loads(decode)

        try:
            english = English.objects.get(pk=content['id'])
            serializer = EnglishSerializer(english, data=decode)

            if not serializer.is_valid():
                response = json_normalizer(
                    code='INTERNAL_SERVER_ERROR',
                    result='Form is not valid.',
                    message=serializer.errors
                )
                self.status = settings.HTTP_CONSTANTS['INTERNAL_SERVER_ERROR']
                return Response(response, status=self.status)

            serializer.save()
            response = json_normalizer(message='English updated successfully.', data=serializer.data)
        except English.DoesNotExist:
            response = json_normalizer(code='NOT_FOUND', result='Not found', message='English not found.')
            self.status = settings.HTTP_CONSTANTS['NOT_FOUND']

        return Response(response, status=self.status)

    @swagger_auto_schema(
        methods=['DELETE'],
        tags=['English'],
        operation_description="Delete english",
        responses=delete_english_schema()
    )
    @api_view(['DELETE'])
    def delete_english(self, english_id):
        try:
            english = English.objects.get(pk=english_id)
            english.delete()
            response = json_normalizer(message='English deleted successfully.')
        except English.DoesNotExist:
            response = json_normalizer(code='NOT_FOUND', result='Not found', message='English not found.')
            self.status = settings.HTTP_CONSTANTS['NOT_FOUND']

        return Response(response, status=self.status)
