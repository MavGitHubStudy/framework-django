import logging
from random import randint

from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
logger = logging.getLogger(__name__)


def get_response(response_parts):
    separator = ': '
    response_str = separator.join(response_parts)
    return response_str


def heads_or_tails(request):
    result = 'HEADS' if randint(0, 1) else 'TAILS'
    response_parts = ["Heads or tails", result]
    response_str = get_response(response_parts)
    logger.info(response_str)
    return HttpResponse(response_str)


def playing_cube_face(request):
    result = str(randint(1, 6))
    response_parts = ["The value of the face of the game cube", result]
    response_str = get_response(response_parts)
    logger.info(response_str)
    return HttpResponse(response_str)


def random_number(request):
    result = str(randint(1, 100))
    response_parts = ["Random number from 0 to 100", result]
    response_str = get_response(response_parts)
    logger.info(response_str)
    return HttpResponse(response_str)
