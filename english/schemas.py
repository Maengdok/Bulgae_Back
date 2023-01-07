from django.http import HttpResponse
from drf_yasg import openapi
from english.serializers import EnglishSerializer


def get_english_list_schema():
    return {
        200: openapi.Response(
            description='English list found.',
            examples=
            {
                'application/json':
                {
                    "code": 200,
                    "result": "Success",
                    "message": "",
                    "data": [
                        {
                            "id": 1,
                            "label": "TestUpdate"
                        },
                    ]
                }
            }
        ),
        405: openapi.Response(
            description='Returns an error when the request methods is not correct.',
            examples=
            {
                'application/json':
                    {
                        "detail": "Method \"POST\" not allowed."
                    }
            }
        )
    }


def get_english_schema():
    return {
        200: openapi.Response(
            description='English found.',
            examples=
            {
                'application/json':
                {
                    "code": 200,
                    "result": "Success",
                    "message": "",
                    "data":
                    {
                        "id": 1,
                        "label": "TestUpdate"
                    }
                }
            }
        ),
        404: openapi.Response(
            description='Returns an error when not found.',
            examples=
            {
                'application/json':
                {
                    'code': 404,
                    'result': 'Not Found',
                    'message': 'English has not been found',
                    'data': 'null',
                },
            }
        ),
        405: openapi.Response(
            description='Returns an error when the request methods is not correct.',
            examples=
            {
                'application/json':
                    {
                        "detail": "Method \"POST\" not allowed."
                    }
            }
        )
    }


def add_english_schema():
    return {
        201: openapi.Response(
            description='English created successfully.',
            examples=
            {
                'application/json':
                    {
                        "code": 201,
                        "result": "Success",
                        "message": "",
                        "data":
                            {
                                "id": 1,
                                "label": "TestUpdate"
                            }
                    }
            }
        ),
        405: openapi.Response(
            description='Returns an error when the request methods is not correct.',
            examples=
            {
                'application/json':
                    {
                        "detail": "Method \"GET\" not allowed."
                    }
            }
        ),
        500: openapi.Response(
            description='Returns an error when the form is not valid.',
            examples=
            {
                'application/json':
                    {
                        'code': 500,
                        'result': 'Form is not valid.',
                        'message': '',
                        'data': 'null',
                    },
            }
        )
    }


def update_english_schema():
    return {
        200: openapi.Response(
            description='English updated successfully.',
            examples=
            {
                'application/json':
                    {
                        "code": 200,
                        "result": "Success",
                        "message": "",
                        "data":
                            {
                                "id": 1,
                                "label": "TestUpdate"
                            }
                    }
            }
        ),
        404: openapi.Response(
            description='Returns an error when not found.',
            examples=
            {
                'application/json':
                    {
                        'code': 404,
                        'result': 'Not Found',
                        'message': 'English has not been found',
                        'data': 'null',
                    },
            }
        ),
        405: openapi.Response(
            description='Returns an error when the request methods is not correct.',
            examples=
            {
                'application/json':
                    {
                        "detail": "Method \"GET\" not allowed."
                    }
            }
        ),
        500: openapi.Response(
            description='Returns an error when the form is not valid.',
            examples=
            {
                'application/json':
                    {
                        'code': 500,
                        'result': 'Form is not valid.',
                        'message': '',
                        'data': 'null',
                    },
            }
        )
    }


def delete_english_schema():
    return {
        200: openapi.Response(
            description='English deleted successfully.',
            examples=
            {
                'application/json':
                {
                    "code": 200,
                    "result": "Success",
                    "message": "",
                    "data": [
                        {
                            "id": 1,
                            "label": "TestUpdate"
                        },
                    ]
                }
            }
        ),
        404: openapi.Response(
            description='Returns an error when not found.',
            examples=
            {
                'application/json':
                    {
                        'code': 404,
                        'result': 'Not Found',
                        'message': 'English has not been found',
                        'data': 'null',
                    },
            }
        ),
        405: openapi.Response(
            description='Returns an error when the request methods is not correct.',
            examples=
            {
                'application/json':
                    {
                        "detail": "Method \"GET\" not allowed."
                    }
            }
        ),
    }
