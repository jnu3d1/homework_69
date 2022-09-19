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
            if isinstance(A, int) and isinstance(B, int):
                answer['answer'] = A + B
            else:
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
            if isinstance(A, int) and isinstance(B, int):
                answer['answer'] = A - B
            else:
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
            if isinstance(A, int) and isinstance(B, int):
                answer['answer'] = A * B
            else:
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
            if isinstance(A, int) and isinstance(B, int):
                if B == 0:
                    return JsonResponse({'error': 'Делить на ноль нельзя'}, status=400)
                answer['answer'] = A / B
            else:
                return JsonResponse({'error': 'Нужно передать числа'}, status=400)
            return JsonResponse(answer)
        else:
            return JsonResponse({'error': 'Данные не переданы'}, status=400)
