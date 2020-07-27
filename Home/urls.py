from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('pattern_picker', pattern_picker, name='pattern_picker'),
    path('delay_slider', delay_slider, name='delay_slider'),
    path('random', random, name='random'),
    path('red', red, name='red'),
    path('green', green, name='green'),
    path('blue', blue, name='blue'),
    path('alpha', alpha, name='alpha'),
    path('size', size, name='size'),
    path('random_decay', random_decay, name='random_decay'),
    path('trail_decay', trail_decay, name='trail_decay'),
]
