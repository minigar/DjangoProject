# from django.shortcuts import render

# # Create your views here.

from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render

from .models import Bb


def index(request):
    print()
    print()
    # return HttpResponse(template.render(context, request))
    bbs = Bb.objects.all()
    return render(request, 'index.html', {'bbs':bbs})