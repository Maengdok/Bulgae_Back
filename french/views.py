from django.conf import settings

from rest_framework.decorators import api_view, schema, action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from drf_yasg.utils import swagger_auto_schema

from services.json_response import json_normalizer
from french.models import French
from .serializers import FrenchSerializer
from .schemas import get_french_schema, get_french_list_schema, add_french_schema, update_french_schema, \
    delete_french_schema


class FrenchViewSet(ViewSet):
    status = settings.HTTP_CONSTANTS['SUCCESS']

    @swagger_auto_schema(methods=['GET'], tags=['French'], operation_description="Get french", responses=get_french_list_schema())
    @api_view(['GET'])
    def french_list(self):
        queryset = French.objects.all()
        serializer = FrenchSerializer(queryset, many=True)
        response = json_normalizer(data=serializer.data)
        return Response(response, status=FrenchViewSet.status)

    @swagger_auto_schema(methods=['GET'], tags=['French'], operation_description="Get french", responses=get_french_schema())
    @api_view(['GET'])
    def get_french(self, french_id):
        try:
            queryset = French.objects.get(pk=french_id)
            serializer = FrenchSerializer(queryset)
            response = json_normalizer(data=serializer.data)
        except French.DoesNotExist:
            response = json_normalizer(code='NOT_FOUND', result='Not found', message='French not found.')
            FrenchViewSet.status = settings.HTTP_CONSTANTS['NOT_FOUND']
        return Response(response, status=FrenchViewSet.status)

    @swagger_auto_schema(
        methods=['POST'],
        tags=['French'],
        operation_description="Add french",
        request_body=FrenchSerializer,
        responses=add_french_schema()
    )
    @parser_classes([JSONParser])
    @api_view(['POST'])
    def add_french(self):
        data = self.data
        serializer = FrenchSerializer(data=data)

        if not serializer.is_valid():
            response = json_normalizer(
                code='INTERNAL_SERVER_ERROR',
                result='Form is not valid.',
                message=serializer.errors
            )
            FrenchViewSet.status = settings.HTTP_CONSTANTS['INTERNAL_SERVER_ERROR']
            return Response(response, status=FrenchViewSet.status)

        serializer.save()
        response = json_normalizer(message='French created successfully.', data=serializer.data)
        return Response(response, status=FrenchViewSet.status)

    @swagger_auto_schema(
        methods=['PUT'],
        tags=['French'],
        operation_description="Update french",
        request_body=FrenchSerializer,
        responses=update_french_schema()
    )
    @api_view(['PUT'])
    def update_french(self):
        data = self.data
        try:
            french = French.objects.get(pk=data['id'])
            serializer = FrenchSerializer(french, data=data, partial=True)

            if not serializer.is_valid():
                response = json_normalizer(
                    code='INTERNAL_SERVER_ERROR',
                    result='Form is not valid.',
                    message=serializer.errors
                )
                FrenchViewSet.status = settings.HTTP_CONSTANTS['INTERNAL_SERVER_ERROR']
                return Response(response, status=FrenchViewSet.status)

            serializer.save()
            response = json_normalizer(message='French updated successfully.', data=serializer.data)
        except French.DoesNotExist:
            response = json_normalizer(code='NOT_FOUND', result='Not found', message='French not found.')
            FrenchViewSet.status = settings.HTTP_CONSTANTS['NOT_FOUND']

        return Response(response, status=FrenchViewSet.status)

    @swagger_auto_schema(
        methods=['DELETE'],
        tags=['French'],
        operation_description="Delete french",
        responses=delete_french_schema()
    )
    @api_view(['DELETE'])
    def delete_french(self, french_id):
        try:
            french = French.objects.get(pk=french_id)
            french.delete()

            queryset = French.objects.all()
            serializer = FrenchSerializer(queryset, many=True)
            response = json_normalizer(message='French deleted successfully.', data=serializer.data)
        except French.DoesNotExist:
            response = json_normalizer(code='NOT_FOUND', result='Not found', message='French not found.')
            FrenchViewSet.status = settings.HTTP_CONSTANTS['NOT_FOUND']

        return Response(response, status=FrenchViewSet.status)
