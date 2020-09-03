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
    page_title = "Profile"
    main_content = "web/profile.html"
    name = "Hanjara CA"
    email = "mangatkk@gmail.com"
    link_instagram = "https://instagram.com/handhyatma"
    link_google = ""
    link_github = "https://github.com/mashanz"
    education = "B.E. in Computer Engineering from Telkom University"
    location = "Singapore"
    notes = "Let's do the best!"
    return render(
        request,
        "web/index.html",
        {
            "page_title": page_title,
            "main_content": main_content,
            "name": name,
            "email": email,
            "link_instagram": link_instagram,
            "link_github": link_github,
            "link_google": link_google,
            "education": education,
            "location": location,
            "notes": notes

        }
    )


def web_line_follower(request):
    page_title = "Line Follower"
    main_content = "web/line_follower.html"
    return render(
        request,
        "web/index.html",
        {
            "page_title": page_title,
            "main_content": main_content
        }
    )


def web_manipulator(request):
    page_title = "Manipulator"
    main_content = "web/blank.html"
    return render(
        request,
        "web/index.html",
        {
            "page_title": page_title,
            "main_content": main_content
        }
    )


def web_humanoid(request):
    page_title = "Humanoid"
    main_content = "web/blank.html"
    return render(
        request,
        "web/index.html",
        {
            "page_title": page_title,
            "main_content": main_content
        }
    )


def web_about_this_page(request):
    page_title = "About This Page"
    main_content = "web/about_this_page.html"
    return render(
        request,
        "web/index.html",
        {
            "page_title": page_title,
            "main_content": main_content
        }
    )
