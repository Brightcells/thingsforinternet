# -*- coding: utf-8 -*-

"""
Copyright (c) 2014 Qimin Huang <kimi.huang@brightcells.com>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

from django.conf import settings
from django.contrib.auth.models import User
from django.core import serializers
from django.core.urlresolvers import reverse
from django.db.models import Q, Count
from django.forms.models import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.encoding import smart_str

import re
import json
import time
import random
import hashlib

from utils.utils import *


pinnimei_list = ['b', 'p', 'm', 'f', 'd', 't', 'n', 'l', 'g', 'k', 'h', 'j', 'q', 'x', 'zh', 'ch', 'sh', 'r', 'z', 'c', 's', 'y', 'w']

labbacklinks = [
    {'name': 'TT4IT', 'url': 'dh:dh', 'para': ''},
    {'name': '实验室', 'url': 'lab:lab', 'para': ''},
]

pinnimeibacklinks = labbacklinks + [{'name': 'Pinnimei', 'url': 'lab:pinnimei', 'para': ''}, ]


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
