import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


# Create your views here.
def add_view(request):
    answer = {}
    if request.method == 'GET':
        return HttpResponse('Передайте числа в формате: {"A": 1234, "B": 5678}')
    elif request.method == 'POST':
        if request.body:
            A, B = json.loads(request.body).values()
            try:
                answer['answer'] = int(A) + int(B)
            except ValueError:
                return JsonResponse({'error': 'Нужно передать числа'}, status=400)
            return JsonResponse(answer)
        else:
            return JsonResponse({'error': 'Данные не переданы'}, status=400)


def subtract_view(request):
    answer = {}
    if request.method == 'GET':
        return HttpResponse('Передайте числа в формате: {"A": 1234, "B": 5678}')
    elif request.method == 'POST':
        if request.body:
            A, B = json.loads(request.body).values()
            try:
                answer['answer'] = int(A) - int(B)
            except ValueError:
                return JsonResponse({'error': 'Нужно передать числа'}, status=400)
            return JsonResponse(answer)
        else:
            return JsonResponse({'error': 'Данные не переданы'}, status=400)


def multiply_view(request):
    answer = {}
    if request.method == 'GET':
        return HttpResponse('Передайте числа в формате: {"A": 1234, "B": 5678}')
    elif request.method == 'POST':
        if request.body:
            A, B = json.loads(request.body).values()
            try:
                answer['answer'] = int(A) * int(B)
            except ValueError:
                return JsonResponse({'error': 'Нужно передать числа'}, status=400)
            return JsonResponse(answer)
        else:
            return JsonResponse({'error': 'Данные не переданы'}, status=400)


def divide_view(request):
    answer = {}
    if request.method == 'GET':
        return HttpResponse('Передайте числа в формате: {"A": 1234, "B": 5678}')
    elif request.method == 'POST':
        if request.body:
            A, B = json.loads(request.body).values()
            try:
                if int(B) == 0:
                    return JsonResponse({'error': 'Делить на ноль нельзя'}, status=400)
                answer['answer'] = int(A) / int(B)
            except ValueError:
                return JsonResponse({'error': 'Нужно передать числа'}, status=400)
            return JsonResponse(answer)
        else:
            return JsonResponse({'error': 'Данные не переданы'}, status=400)
