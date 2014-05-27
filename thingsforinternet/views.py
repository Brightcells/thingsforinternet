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
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.utils.encoding import smart_str

import re
import json
import time
import random
import hashlib

from utils.utils import *


def search(request):
    '''
    usr, ui = getUsrUI(request)
    _query = request.POST.get('query', '')
    doubanSearchUrl = 'http://book.douban.com/subject_search?search_text=' + _query
    reDict = {'usr': usr, 'dsu': doubanSearchUrl}
    return render_to_response('common/dquery.html', reDict)
    '''
    _query = request.POST.get('query', '')
    doubanSearchUrl = 'http://book.douban.com/subject_search?search_text='
    return HttpResponseRedirect(doubanSearchUrl+_query)