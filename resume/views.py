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
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.forms.models import model_to_dict
from django.shortcuts import render, redirect

from dh.models import *
from resume.models import ResumeInfo
from resume.forms import ResumeInfoModelForm

from utils.utils import *


RESUMEBACKLINKS = [
    {'name': 'TT4IT', 'url': 'dh:dh', 'para': ''},
    {'name': '简历', 'url': 'resume:resume', 'para': ''},
]

RESUME2BACKLINKS = RESUMEBACKLINKS + [{'name': '简历', 'url': 'resume:resume2home', 'para': ''}, ]


def pages(setlist, p):
    """ Paginator """

    paginator = Paginator(setlist, settings.TIPS_PER_PAGE)
    try:
        return paginator.page(p)
    except:
        return paginator.page(1)


def getResumeDict(request):
    return {'backlinks': RESUMEBACKLINKS, 'lists': getFunc(request, 'resume'), 'usr': getUsr(request)}


def getResume2Dict(request):
    return {'backlinks': RESUME2BACKLINKS, 'lists': getNav(request, 'resume2'), 'usr': getUsr(request)}


def resume(request):
    """ APP Resume's home """

    return render(request, 'resume/resume.html', getResumeDict(request))


def resume2home(request):
    """ Function Resume2's home - Upload、Manage、Scan resume of development """

    return redirect(reverse('resume:resume2mine'))


def resume2mine(request):
    try:
        mineresume = ResumeInfo.objects.get(user=getUI(getUsr(request)), display=True).data
    except:
        mineresume = {}
    return render(
        request,
        'resume/resume2/mine.html',
        dict(resume=mineresume, **getResume2Dict(request))
    )


def resume2edit(request):
    if request.method == "POST":
        mineresume, created = ResumeInfo.objects.get_or_create(user=getUI(getUsr(request)), display=True)
        form = ResumeInfoModelForm(request.POST, request.FILES, instance=mineresume)
        if form.is_valid():
            form.save()

    try:
        mineresume = model_to_dict(ResumeInfo.objects.get(user=getUI(getUsr(request)), display=True))
        form = ResumeInfoModelForm(mineresume)
    except:
        form = ResumeInfoModelForm()

    return render(
        request,
        'resume/resume2/edit.html',
        dict(form=form, **getResume2Dict(request))
    )
