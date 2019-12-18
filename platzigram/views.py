"""
Platzigram views
"""
# Django
from django.http import HttpResponse
from django.http import JsonResponse

# utilities
from datetime import datetime


def hello_world(request):
    """Return current server time"""
    return HttpResponse('Oh, hi! Current server time is {1}{0}'.format(
        datetime.now().strftime('%b %dth, %Y - %H:%M hrs'), 'aca estoy ',
    ))


def sorted_by_get(request):
    """
    En esta view agarramos los parametros que se estan enviando por la URL
    los organizamos y los devolvemos en JSON, normalmente se crearia el
    diccionario que vamos a devolver y despues lo pasereamos con json.dumps()
    ej:
        data = {
            'status': 'ok',
            'numbers': sorted_ints,
            'message': 'Integers sorted successfully.'
        }
        return HttpResponse(
            json.dumps(data), content_type="application/json"
        )
    """
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_ints = sorted(numbers)
    # El argumento safe=False es para permitir objetos diferentes a dict
    response = JsonResponse({
        'status': 'ok',
        'numbers': sorted_ints,
        'message': 'Integers sorted successfully.'
        },
    )
    return HttpResponse(response, content_type="application/json")


def say_hi(request, name, age):
    """name y age se deben enviar en esta view devido a que en la url lo
    estamos enviando ... esta view validara si el usuario es mayor a 12
    anios
    """
    if age < 12:
        message = 'Sorry {}, you are not allowed here'.format(name)
    else:
        message = 'Hello, {}! Welcome to Platzigram'.format(name)
    return HttpResponse(message)
