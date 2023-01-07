from drf_yasg import openapi
from english.serializers import EnglishSerializer


def get_english_list_schema():
    return {
        200: openapi.Response('English list found.', EnglishSerializer(many=True)),
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
        200: openapi.Response('English found.', EnglishSerializer),
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
        201: openapi.Response('English created successfully.', EnglishSerializer),
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
                        'dta': 'null',
                    },
            }
        )
    }


def update_english_schema():
    return {
        200: openapi.Response('English updated successfully.', EnglishSerializer),
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
                        'dta': 'null',
                    },
            }
        )
    }


def delete_english_schema():
    return {
        200: openapi.Response('English deleted successfully.', EnglishSerializer(many=True)),
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
