from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
# Create your views here.


def test_api(request):
    print("OH")
    x = [1, 4, 2, 5, 7, 8, 6, 3, 8, 7, 9, 8, 0]
    k = 0
    for i in x:
        k += i
    response = JsonResponse(
        {
            'foo': 'bar',
            'x': x,
            'k': k
        }
    )
    return response
