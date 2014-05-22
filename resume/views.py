# Create your views here.
# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from dh.models import *

from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse

from django.db.models import Q
from django.db.models import Count

from django.utils import simplejson
from django.core import serializers
from django.utils.encoding import smart_str
from django.forms.models import model_to_dict

import re
import json
import time
import random
import hashlib

from utils.utils import *


def resume(request):
    reDict = {}
    response = render_to_response('resume/resume.html', reDict)
    return response