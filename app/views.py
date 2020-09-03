# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django import template


@login_required(login_url="/login/")
def index(request):
    return render(request, "index.html")


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]
        html_template = loader.get_template(load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:

        html_template = loader.get_template('page-500.html')
        return HttpResponse(html_template.render(context, request))


def ini_api(request):
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


def ini_current_datetime(request):
    # response = HttpResponse("Here's the text of the Web page.")
    response = HttpResponse("Text only, please.", content_type="text/plain")
    # response = HttpResponse(b'Bytestrings are also accepted.')
    # response = HttpResponse(memoryview(b'Memoryview as well.'))
    return response


def web_index(request):
    return render(request, "web/index.html", {"page_title": "Profile"})
