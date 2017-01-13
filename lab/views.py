# -*- coding: utf-8 -*-

import json
import random

from django.http import HttpResponse
from django.shortcuts import render

from utils.tt4it_utils import *


pinnimei_list = ['b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'zh', 'ch', 'sh', 'r', 'z', 'c', 's', 'y', 'w']

labbacklinks = [
    {'name': 'TT4IT', 'url': 'dh:dh', 'para': ''},
    {'name': '实验室', 'url': 'lab:lab', 'para': ''},
]
pinnimeibacklinks = labbacklinks + [{'name': 'Pinnimei', 'url': 'lab:pinnimei', 'para': ''}]


def getLabDict(request):
    usr, ui = getUsrUI(request)
    display_bg, slide_image_classify = (ui.display_bg, ui.classify) if ui else (True, '')

    return {
        'backlinks': labbacklinks,
        'lists': getFunc(request, 'lab'),
        'usr': usr,
        'display_bg': display_bg,
        'slide_image_classify': slide_image_classify
    }


def getPinnimeiDict(request):
    usr, ui = getUsrUI(request)
    display_bg, slide_image_classify = (ui.display_bg, ui.classify) if ui else (True, '')

    return {
        'backlinks': pinnimeibacklinks,
        'usr': usr,
        'display_bg': display_bg,
        'slide_image_classify': slide_image_classify
    }


def lab(request):
    """ APP Lab """

    return render(request, 'lab.html', getLabDict(request))


def pinnimei(request):
    """ Lab Project Pinnime - A smail word game to push consonant """

    return render(
        request,
        'lab/pinnimei.html',
        dict(consonants=random.sample(pinnimei_list, 5), **getPinnimeiDict(request))
    )


def check_word(request):
    word = request.POST.get('word', '')
    consonants = request.POST.get('consonants', '')

    if word:
        from xpinyin import Pinyin
        wlist = Pinyin().get_pinyin(word).split('-')

        # Some word isn't correct such as '种'
        # from uuslug import slugify
        # wlist = slugify(word).split('-')

        data = []
        for pinyin in wlist:
            if ';' + pinyin[0:2] + '&' in consonants:
                data.append(pinyin[0:2])
            elif ';' + pinyin[0] + '&' in consonants:
                data.append(pinyin[0])

        if len(wlist) == len(data):
            data = [d for d in data if ';' + d + '&' not in consonants.split(',')[0]]
            reDict = {'status': True, 'data': data}
        else:
            reDict = {'status': False}
    else:
        reDict = {'status': False}
    return HttpResponse(json.dumps(reDict))
