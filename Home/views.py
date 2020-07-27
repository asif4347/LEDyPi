from django.http import JsonResponse
from django.shortcuts import render
from getenv import env
import os


def get_val_from_env(key_name: str):
    return env(key_name)


def get_metior_value():
    return bool(env('show_metior'))


def index(request):
    # if you want to get environment variable
    # env_variable = get_val_from_env('my_env')
    # print(env_variable)
    drop_down = [
        {
            'label': 'Color Wipe',
            'value': 'CW'
        },
        {
            'label': 'Color Display',
            'value': 'CD'
        }
    ]
    random = True  # set values as per you want below if random
    random_decay = True
    slider_values = {
        'delay': {
            'min': 0,
            'max': 100,
            'current': 23
        },
        'red': {
            'min': 0,
            'max': 255,
            'current': 23
        },
        'green': {
            'min': 0,
            'max': 255,
            'current': 23
        },
        'blue': {
            'min': 0,
            'max': 255,
            'current': 40

        },
        'alpha': {
            'min': 0,
            'max': 255,
            'current': 23
        },
        'size': {
            'min': 0,
            'max': 100,
            'current': 50
        },
        'trail_decay': {
            'min': 0,
            'max': 100,
            'current': 10
        }

    }

    context = {
        'sliders': slider_values,
        "drop_down": drop_down,
        'random': random,
        'random_decay': random_decay,
        'show_metior': get_val_from_env('show_metior')
    }
    return render(request, 'home/index.html', context=context)


def pattern_picker(request):
    value = request.GET.get('value')
    print(value)
    # Your code here
    response = {
        'success': True,
        'value': value,
        'show_metior': get_val_from_env('show_metior')
    }
    return JsonResponse(response, safe=False)


def delay_slider(request):
    value = int(request.GET.get('value'))
    print(value)
    # Your code here
    response = {
        'success': True,
        'value': value,
        'show_metior': get_val_from_env('show_metior')
    }
    return JsonResponse(response, safe=False)


def random(request):
    value = request.GET.get('value')
    print(value)
    # Your code here
    response = {
        'success': True,
        'value': value,
        'show_metior': get_val_from_env('show_metior')
    }
    return JsonResponse(response, safe=False)


def red(request):
    value = int(request.GET.get('value'))
    print(value)
    # Your code here
    response = {
        'success': True,
        'value': value,
        'show_metior': get_val_from_env('show_metior')
    }
    return JsonResponse(response, safe=False)


def green(request):
    value = int(request.GET.get('value'))
    print(value)
    # Your code here
    response = {
        'success': True,
        'value': value,
        'show_metior': get_val_from_env('show_metior')
    }
    return JsonResponse(response, safe=False)


def blue(request):
    value = int(request.GET.get('value'))
    print(value)
    # Your code here
    response = {
        'success': True,
        'value': value,
        'show_metior': get_val_from_env('show_metior')
    }
    return JsonResponse(response, safe=False)


def alpha(request):
    value = int(request.GET.get('value'))
    print(value)
    # Your code here
    # just as example to show metior
    if value > 30:
        os.environ['show_metior'] = "True"  # envoirnment accpets only strings
    else:
        os.environ['show_metior'] = "False"

    response = {
        'success': True,
        'value': value,
        'show_metior': get_val_from_env('show_metior')
    }
    return JsonResponse(response, safe=False)


def size(request):
    value = int(request.GET.get('value'))
    print(value)
    # Your code here
    response = {
        'success': True,
        'value': value,
        'show_metior': get_val_from_env('show_metior')
    }
    return JsonResponse(response, safe=False)


def random_decay(request):
    value = request.GET.get('value')
    print(value)
    # Your code here
    response = {
        'success': True,
        'value': value,
        'show_metior': get_val_from_env('show_metior')
    }
    return JsonResponse(response, safe=False)


def trail_decay(request):
    value = int(request.GET.get('value'))
    print(value)
    # Your code here
    response = {
        'success': True,
        'value': value,
        'show_metior': get_val_from_env('show_metior')
    }
    return JsonResponse(response, safe=False)
