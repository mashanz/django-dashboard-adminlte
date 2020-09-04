from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django import template
from django.utils.safestring import mark_safe
import datetime
from .forms import AddPersonForm
from .models import PersonModel
now = datetime.datetime.now()
version = "1.0.0"


def unrivalry_add_person(request):
    page_title = "Add Person"
    main_content = "web/add_person.html"
    form = AddPersonForm(request.POST or None)

    person = PersonModel.objects.all()

    msg = None
    success = False

    if request.method == "POST":
        if form.is_valid():
            full_name = form.cleaned_data.get("full_name")
            shirt_size = form.cleaned_data.get("shirt_size")
            success = True
            # AddPersonForm(full_name=full_name, shirt_size=shirt_size)
            PersonModel(full_name=full_name, shirt_size=shirt_size)
            form.save()
        else:
            msg = 'Form is not valid'
    else:
        form = AddPersonForm()

    return render(
        request,
        "web/index.html",
        {
            "page_title": page_title,
            "main_content": main_content,
            "year": now.year,
            "version": version,
            "form": form,
            "msg": msg,
            "success": success,
            "person": person
        }
    )


def unrivalry_delete_person(request):
    if request.POST:
        pass


def unrivalry_api(request):
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


def unrivalry_pages(request):
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
