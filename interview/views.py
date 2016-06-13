# -*- coding: utf-8 -*-

from django.shortcuts import render


def interview(request):
    return render(request, 'interview/interview.html', {})
