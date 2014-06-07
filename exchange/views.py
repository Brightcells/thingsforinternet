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
from django.shortcuts import render, redirect

from dh.models import *
from exchange.decorators import tt_login_required
from exchange.forms import TipsModelForm
from exchange.models import Tips, UserTips

from utils.utils import *


EXCHANGEBACKLINKS = [
    {'name': 'TT4IT', 'url': 'dh:dh', 'para': ''},
    {'name': '交流', 'url': 'exchange:exchange', 'para': ''},
]

TIPSBACKLINKS = EXCHANGEBACKLINKS + [{'name': 'TIPS', 'url': 'exchange:tipshome', 'para': ''}, ]


def pages(setlist, p):
    """ Paginator """

    paginator = Paginator(setlist, settings.TIPS_PER_PAGE)
    try:
        return paginator.page(p)
    except:
        return paginator.page(1)


def getResourcesDict(request):
    usr, ui = getUsrUI(request)
    display_bg = ui.display_bg if ui else True
    return {'backlinks': EXCHANGEBACKLINKS, 'lists': getFunc(request, 'exchange'), 'usr': usr, 'display_bg': display_bg}


def getTipsDict(request):
    usr, ui = getUsrUI(request)
    display_bg = ui.display_bg if ui else True
    return {'backlinks': TIPSBACKLINKS, 'lists': getNav(request, 'tips'), 'usr': usr, 'display_bg': display_bg}


def exchange(request):
    """ APP Exchange's home """

    return render(request, 'exchange/exchange.html', getResourcesDict(request))


def tipshome(request):
    """ Function Tips's home - Upload、Manage、Scan tips of development """

    return redirect(reverse('exchange:tipsall'))


def lcr(obj, num, flag):
    if 't' == flag:
        return [obj[i].data for i in xrange(len(obj)) if i % 3 == num]
    else:
        return [obj[i].tips.data for i in xrange(len(obj)) if i % 3 == num]


def lcrdict(obj, flag):
    return {'left': lcr(obj, 0, flag), 'center': lcr(obj, 1, flag), 'right': lcr(obj, 2, flag)}


def tipsrecord(request, p=1):
    status = False
    user = getUI(getUsr(request))

    if request.method == 'GET':
        form = TipsModelForm()
    else:
        form = TipsModelForm(request.POST, request=request)
        if form.is_valid():
            cleaned_data = form.cleaned_data

            tips = cleaned_data['tips']
            tag = cleaned_data['tag']
            url = cleaned_data['url']

            t, created = Tips.objects.get_or_create(tips=tips, tag=tag, url=url)
            if created:
                t.author = user
                t.save()
                UserTips.objects.create(tips=t, user=user)
            else:
                UserTips.objects.create(tips=t, user=user, status=False)

            form = TipsModelForm()
            status = True

    minetips = UserTips.objects.filter(user=user, tips__display=True).order_by('-create_time')
    tips = pages(minetips, int(p))

    return render(
        request,
        'exchange/tips/record.html',
        dict(lcrdict(tips.object_list, 'ut'), pages=tips, next_url='exchange:tipsmine', form=form, status=status, **getTipsDict(request))
    )


@tt_login_required
def tipsmine(request, p=1):
    minetips = UserTips.objects.filter(user=getUI(getUsr(request)), tips__display=True).order_by('-create_time')
    tips = pages(minetips, int(p))
    return render(
        request,
        'exchange/tips/mine.html',
        dict(lcrdict(tips.object_list, 'ut'), pages=tips, next_url='exchange:tipsmine', **getTipsDict(request))
    )


def tipsall(request, p=1):
    alltips = Tips.objects.filter(display=True).order_by('-create_time')
    tips = pages(alltips, int(p))
    return render(
        request,
        'exchange/tips/all.html',
        dict(lcrdict(tips.object_list, 't'), pages=tips, next_url='exchange:tipsall', **getTipsDict(request))
    )


def tipssearch(request, p=1):
    _query = request.GET.get('query', '')
    searchtips = Tips.objects.filter(Q(tips__contains=_query) | Q(tag__contains=_query) | Q(url__contains=_query), display=True).order_by('-create_time')
    tips = pages(searchtips, int(p))
    return render(
        request,
        'exchange/tips/search.html',
        dict(lcrdict(tips.object_list, 't'), pages=tips, next_url='exchange:tipssearch', query='?query=' + _query, **getTipsDict(request))
    )


def discuss(request, tipid):
    tip = Tips.objects.get(pk=tipid, display=True).data
    return render(
        request,
        'exchange/tips/discuss.html',
        dict(tip=tip, **getTipsDict(request))
    )


def forumhome(request):
    """ Function Forum's home """

    return render(request, 'exchange/tips/tipshome.html', dict(**getTipsDict(request)))