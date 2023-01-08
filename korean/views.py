from django.conf import settings

from rest_framework.decorators import api_view, schema, action
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from drf_yasg.utils import swagger_auto_schema

from services.json_response import json_normalizer
from korean.models import Korean
from .serializers import KoreanSerializer
from .schemas import get_korean_schema, get_korean_list_schema, add_korean_schema, update_korean_schema, \
    delete_korean_schema


class KoreanViewSet(ViewSet):
    status = settings.HTTP_CONSTANTS['SUCCESS']

    @swagger_auto_schema(
        methods=['GET'],
        tags=['Korean'],
        operation_description="Get korean",
        responses=get_korean_list_schema()
    )
    @api_view(['GET'])
    def korean_list(self):
        queryset = Korean.objects.all()
        serializer = KoreanSerializer(queryset, many=True)
        response = json_normalizer(data=serializer.data)
        return Response(response, status=KoreanViewSet.status)

    @swagger_auto_schema(
        methods=['GET'],
        tags=['Korean'],
        operation_description="Get korean",
        responses=get_korean_schema()
    )
    @api_view(['GET'])
    def get_korean(self, korean_id):
        try:
            queryset = Korean.objects.get(pk=korean_id)
            serializer = KoreanSerializer(queryset)
            response = json_normalizer(data=serializer.data)
        except Korean.DoesNotExist:
            response = json_normalizer(code='NOT_FOUND', result='Not found', message='Korean not found.')
            KoreanViewSet.status = settings.HTTP_CONSTANTS['NOT_FOUND']
        return Response(response, status=KoreanViewSet.status)

    @swagger_auto_schema(
        methods=['POST'],
        tags=['Korean'],
        operation_description="Add korean",
        request_body=KoreanSerializer,
        responses=add_korean_schema()
    )
    @parser_classes([JSONParser])
    @api_view(['POST'])
    def add_korean(self):
        data = self.data
        serializer = KoreanSerializer(data=data)

        if not serializer.is_valid():
            response = json_normalizer(
                code='INTERNAL_SERVER_ERROR',
                result='Form is not valid.',
                message=serializer.errors
            )
            KoreanViewSet.status = settings.HTTP_CONSTANTS['INTERNAL_SERVER_ERROR']
            return Response(response, status=KoreanViewSet.status)

        serializer.save()
        response = json_normalizer(message='Korean created successfully.', data=serializer.data)
        return Response(response, status=KoreanViewSet.status)

    @swagger_auto_schema(
        methods=['PUT'],
        tags=['Korean'],
        operation_description="Update korean",
        request_body=KoreanSerializer,
        responses=update_korean_schema()
    )
    @api_view(['PUT'])
    def update_korean(self):
        data = self.data
        try:
            korean = Korean.objects.get(pk=data['id'])
            serializer = KoreanSerializer(korean, data=data, partial=True)

            if not serializer.is_valid():
                response = json_normalizer(
                    code='INTERNAL_SERVER_ERROR',
                    result='Form is not valid.',
                    message=serializer.errors
                )
                KoreanViewSet.status = settings.HTTP_CONSTANTS['INTERNAL_SERVER_ERROR']
                return Response(response, status=KoreanViewSet.status)

            serializer.save()
            response = json_normalizer(message='Korean updated successfully.', data=serializer.data)
        except Korean.DoesNotExist:
            response = json_normalizer(code='NOT_FOUND', result='Not found', message='Korean not found.')
            KoreanViewSet.status = settings.HTTP_CONSTANTS['NOT_FOUND']

        return Response(response, status=KoreanViewSet.status)

    @swagger_auto_schema(
        methods=['DELETE'],
        tags=['Korean'],
        operation_description="Delete korean",
        responses=delete_korean_schema()
    )
    @api_view(['DELETE'])
    def delete_korean(self, korean_id):
        try:
            korean = Korean.objects.get(pk=korean_id)
            korean.delete()

            queryset = Korean.objects.all()
            serializer = KoreanSerializer(queryset, many=True)
            response = json_normalizer(message='Korean deleted successfully.', data=serializer.data)
        except Korean.DoesNotExist:
            response = json_normalizer(code='NOT_FOUND', result='Not found', message='Korean not found.')
            KoreanViewSet.status = settings.HTTP_CONSTANTS['NOT_FOUND']

        return Response(response, status=KoreanViewSet.status)
