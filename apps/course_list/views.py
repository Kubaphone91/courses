# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Course
# Create your views here.

def index(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'course_list/index.html', context)

def add_course(request):
    Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect('/')

def confirm(request, id):
    context = {
        'courses': Course.objects.filter(id=id)
    }
    return render(request, 'course_list/destroy.html', context)

def delete_course(request, id):
    Course.objects.filter(id=id).delete()
    return redirect('/')
