# -*- coding: utf-8 -*-

from django.shortcuts import render


def offer(request):
    return render(request, 'offer/offer.html', {})
