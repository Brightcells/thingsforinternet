# Create your views here.
# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib.auth.models import User
from django.core import serializers
from django.core.urlresolvers import reverse
from django.db.models import Q, Count
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.utils.encoding import smart_str

from accounts.models import UserInfo

import re
import json
import time
import random
import hashlib

from utils.utils import *


def dh(request):
    backlinks = [{'name': 'TT4IT', 'url': 'dh:dh', 'para': ''}]
    reDict = {'backlinks': backlinks, 'lists': getApp(request), 'usr': getUsr(request)}
    return render_to_response('dh/dh.html', reDict)
