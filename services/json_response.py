from django.conf import settings


def json_normalizer(code='SUCCESS', result='Success', message='', data=None):
    if code not in list(settings.HTTP_CONSTANTS.keys()):
        json_normalizer(code='NOT_FOUND', result='Not Found', message='Code not found.', data={'wrong_code': code})

    return {
            'code': settings.HTTP_CONSTANTS[code],
            'result': result,
            'message': message,
            'data': data
        }
