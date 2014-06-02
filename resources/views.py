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
from django.db.models import Q
from django.forms.models import model_to_dict
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from accounts.models import UserInfo
from resources.decorators import tt_login_required
from resources.models import *
from resources.forms import WebSiteSubmitModelForm, ApiModelForm

from utils.utils import *


spp = settings.SITE_PER_PAGE

RESOURCESBACKLINKS = [
    {'name': 'TT4IT', 'url': 'dh:dh', 'para': ''},
    {'name': '资源', 'url': 'resources:resources', 'para': ''},
]

ITGPSBACKLINKS = RESOURCESBACKLINKS + [{'name': 'ITGPS', 'url': 'resources:itgpshome', 'para': ''}, ]

APIBACKLINKS = RESOURCESBACKLINKS + [{'name': 'API', 'url': 'resources:apihome', 'para': ''}, ]


def pages(setlist, p):
    paginator = Paginator(setlist, settings.TIPS_PER_PAGE)
    try:
        return paginator.page(p)
    except:
        return paginator.page(1)


def getResourcesDict(request):
    return {'backlinks': RESOURCESBACKLINKS, 'lists': getFunc(request, 'resources'), 'usr': getUsr(request)}


def getItgpsDict(request):
    return {'backlinks': ITGPSBACKLINKS, 'lists': getNav(request, 'itgps'), 'usr': getUsr(request)}


def getApiDict(request):
    return {'backlinks': APIBACKLINKS, 'lists': getNav(request, 'api'), 'usr': getUsr(request)}


def resources(request):
    """ APP Resources's home """

    return render(request, 'resources/resources.html', getResourcesDict(request))


def itgpshome(request):
    """ Function ITGPS's home - A Navigation Site for IT """

    reDict = {'favs': getFavoriteSite(request)}
    return render(request, 'resources/itgps/itgps.html', dict(reDict, **getItgpsDict(request)))


def itgps_hottest_lastest(request):
    reDict = {'hottests': getHottestSite(request, spp), 'lasttests': getLasttestSite(request, spp)}
    return render(request, 'resources/itgps/hottest_lastest.html', dict(reDict, **getItgpsDict(request)))


def getHottestSite(request, _num):
    hotSiteSetList = WebSiteInfo.objects.filter(display=True).order_by('-visit')[:_num]
    hottests = []
    for hotSiteSet in hotSiteSetList:
        hotSiteDict = model_to_dict(hotSiteSet)
        hotSiteDict['flike'] = getLikeFlag(request, hotSiteSet.id, True)
        hotSiteDict['ffav'] = getFavFlag(request, hotSiteSet.id)
        hottests.append(hotSiteDict)
    return hottests


def getLasttestSite(request, _num):
    lastSiteSetList = WebSiteInfo.objects.filter(display=True).order_by('-create_time')[:_num]
    lasttests = []
    for lastSiteSet in lastSiteSetList:
        lastSiteDict = model_to_dict(lastSiteSet)
        lastSiteDict['flike'] = getLikeFlag(request, lastSiteSet.id, True)
        lastSiteDict['ffav'] = getFavFlag(request, lastSiteSet.id)
        lasttests.append(lastSiteDict)
    return lasttests


def getFavoriteSite(request):
    if not None:
        favSiteSetList = Favorite.objects.filter(user__username=getUsr(request))
    else:
        favSiteSetList = Favorite.objects.filter(host=getIP(request))
    favsites = []
    for favSiteSet in favSiteSetList:
        favSiteDict = model_to_dict(favSiteSet)
        favSiteDict['site'] = favSiteSet
        favSiteDict['flike'] = getLikeFlag(request, favSiteSet.website.id, True)
        favSiteDict['ffav'] = getFavFlag(request, favSiteSet.website.id)
        favsites.append(favSiteDict)
    return favsites


def getSearchSite(request, _query):
    searchSiteSetList = WebSiteInfo.objects.filter(Q(url__contains=_query) | Q(name__contains=_query) | Q(logo__contains=_query) | Q(descr__contains=_query) | Q(tag__contains=_query) | Q(srcode__contains=_query), display=True).order_by('-create_time')
    searchs = []
    for searchSiteSet in searchSiteSetList:
        searchSiteDict = model_to_dict(searchSiteSet)
        searchSiteDict['flike'] = getLikeFlag(request, searchSiteSet.id, True)
        searchSiteDict['ffav'] = getFavFlag(request, searchSiteSet.id)
        searchs.append(searchSiteDict)
    return searchs


def getLikeFlag(request, siteid, _flag):
    '''
        @function: get the flag of whether usr and ip liked the site, and usr first
        @paras:
            siteid - the site.pk, unique identification the site
            _flag - Like:True, Unlike:False
        @returns: True or False boolean
    '''
    if 'usr' in request.COOKIES:
        return Like.objects.filter(user__username=request.COOKIES['usr'], flag=_flag, website__id=siteid).count() != 0
    else:
        return Like.objects.filter(host=getIP(request), flag=_flag, website__id=siteid).count() != 0


def getFavFlag(request, siteid):
    '''
        @function: get the flag of whether usr and ip favorite the, and usr first
        @paras:
            sited - the site.pk, unique identification the site
        @returns: True or False boolean
    '''
    if 'usr' in request.COOKIES:
        return Favorite.objects.filter(user__username=request.COOKIES['usr'], website__id=siteid).count() != 0
    else:
        return Favorite.objects.filter(host=getIP(request), website__id=siteid).count() != 0


def getCsySite(request, _nav, _num, _flag, _id):
    '''
        @function: get site list for different classify in a certain nav
        @paras:
            _nav - the certain nav for which to get csy site
            _num - limit num of site to get
            _flag - 0 for all, 1 for only
        @returns: csysite dict
    '''
    if _flag:
        csySetList = ClassifyInfo.objects.filter(id=_id, display=True)
    else:
        csySetList = ClassifyInfo.objects.filter(nav__name=string.upper(_nav), display=True).order_by('position')
    csysite = []
    for csySet in csySetList:
        csyDict = model_to_dict(csySet)
        csySiteSetList = csySet.csysite_set.filter(display=True).order_by('-website__visit')
        csySiteSetList = csySiteSetList[:_num] if _num else csySiteSetList
        site = []
        for csySiteSet in csySiteSetList:
            csySiteDict = model_to_dict(csySiteSet)
            csySiteDict['site'] = csySiteSet
            csySiteDict['flike'] = getLikeFlag(request, csySiteSet.website.id, True)
            csySiteDict['ffav'] = getFavFlag(request, csySiteSet.website.id)
            site.append(csySiteDict)
        csyDict['siteSet'] = site
        csysite.append(csyDict)
    return csysite


def itgps(request, _nav):
    reDict = {'csysite': getCsySite(request, _nav, spp, 0, '')}
    return render(request, 'resources/itgps/scroll.html', dict(reDict, **getItgpsDict(request)))


def csysite(request, _id):
    reDict = {'csysite': getCsySite(request, '', '', 1, _id)}
    return render(request, 'resources/itgps/scroll.html', dict(reDict, **getItgpsDict(request)))


def visit(request):
    _siteid = request.POST.get('siteid', '')
    try:
        wsi = WebSiteInfo.objects.get(id=_siteid)
        wsi.visit += 1
        wsi.save()
        return HttpResponse(json.dumps({'code': '200', 'msg': 'Increase visit success!'}))
    except:
        info = sys.exc_info()
        return HttpResponse(json.dumps({'code': '201', 'msg': str(info[1])}))


def favorite(request):
    _siteid = request.POST.get('siteid', '')
    try:
        wsi = WebSiteInfo.objects.get(id=_siteid)
        _usr, _host = getUsrHost(request)
        u = UserInfo.objects.filter(username=_usr)
        if 1 == u.count():
            ui = getUI(_usr)
            try:
                Favorite.objects.get(website=wsi, user=ui).delete()
                wsi.fav -= 1
                wsi.save()
                Log.objects.create(user=ui, host=_host, website=wsi, descr="Cancel Favorite")
                return HttpResponse(json.dumps({'code': '302', 'msg': 'Cancel fav success!'}))
            except:
                Favorite.objects.create(website=wsi, user=ui, host=_host)
                wsi.fav += 1
                wsi.save()
                Log.objects.create(user=ui, host=_host, website=wsi, descr="Insert Favorite")
                return HttpResponse(json.dumps({'code': '300', 'msg': 'Increase fav success!'}))
        else:
            try:
                Favorite.objects.get(website=wsi, host=_host).delete()
                wsi.fav -= 1
                wsi.save()
                Log.objects.create(host=_host, website=wsi, descr="Cancel Favorite")
                return HttpResponse(json.dumps({'code': '302', 'msg': 'Cancel fav success!'}))
            except:
                Favorite.objects.create(website=wsi, host=_host)
                wsi.fav += 1
                wsi.save()
                Log.objects.create(host=_host, website=wsi, descr="Insert Favorite")
                return HttpResponse(json.dumps({'code': '300', 'msg': 'Increase fav success!'}))
    except:
        info = sys.exc_info()
        return HttpResponse(json.dumps({'code': '301', 'msg': str(info[1])}))


def like(request):
    _siteid = request.POST.get('siteid', '')
    try:
        wsi = WebSiteInfo.objects.get(id=_siteid)
        _usr, _host = getUsrHost(request)
        u = UserInfo.objects.filter(username=_usr)
        if 1 == u.count():
            ui = getUI(_usr)
            try:
                Like.objects.get(website=wsi, user=ui).delete()
                wsi.like -= 1
                wsi.save()
                Log.objects.create(user=ui, host=_host, website=wsi, descr="Cancel Like")
                return HttpResponse(json.dumps({'code': '402', 'msg': 'Cancel like success!'}))
            except:
                Like.objects.create(website=wsi, user=ui, host=_host)
                wsi.like += 1
                wsi.save()
                Log.objects.create(user=ui, host=_host, website=wsi, descr="Insert Like")
                return HttpResponse(json.dumps({'code': '400', 'msg': 'Increase like success!'}))
        else:
            try:
                Like.objects.get(website=wsi, host=_host).delete()
                wsi.like -= 1
                wsi.save()
                Log.objects.create(host=_host, website=wsi, descr="Cancel Like")
                return HttpResponse(json.dumps({'code': '402', 'msg': 'Cancel like success!'}))
            except:
                Like.objects.create(website=wsi, host=_host)
                wsi.like += 1
                wsi.save()
                Log.objects.create(host=_host, website=wsi, descr="Insert Like")
                return HttpResponse(json.dumps({'code': '400', 'msg': 'Increase like success!'}))
    except:
        info = sys.exc_info()
        return HttpResponse(json.dumps({'code': '401', 'msg': str(info[1])}))


def getSiteInfo(request, siteid):
    siteSetList = WebSiteInfo.objects.filter(id=siteid, display=True)
    sites = []
    for siteSet in siteSetList:
        siteSetDict = model_to_dict(siteSet)
        siteSetDict['flike'] = getLikeFlag(request, siteSet.id, True)
        siteSetDict['ffav'] = getFavFlag(request, siteSet.id)
        sites.append(siteSetDict)
    return sites


def getSiteRelatedInfo(request, siteid):
    return WebsiteRelatedInfo.objects.filter(website__id=siteid, display=True)


def discuss(request, siteid):
    reDict = {'sites': getSiteInfo(request, siteid), 'relateds': getSiteRelatedInfo(request, siteid)}
    return render(request, 'resources/itgps/discuss.html', dict(reDict, **getItgpsDict(request)))


def itgpssearch(request):
    _query = request.GET.get('query', '')
    search_result = getSearchSite(request, _query)
    if len(search_result):
        reDict = {'searchs': search_result}
        return render(request, 'resources/itgps/search.html', dict(reDict, **getItgpsDict(request)))
    else:
        return HttpResponseRedirect(settings.GOOGLE_SEARCH + _query)


def itgpssubmit(request, p=1):
    if request.method == 'GET':
        form = WebSiteSubmitModelForm()
    else:
        form = WebSiteSubmitModelForm(request.POST)
        if form.is_valid():
            form.save()

    allwsss = WebSiteSubmit.objects.all().order_by('-create_time')
    return render(
        request,
        'resources/itgps/submit.html',
        dict(form=form, pages=pages(allwsss, int(p)), next_url='resources:itgpssubmit', **getItgpsDict(request))
    )


def apihome(request):
    """ Function API's home - Upload、Manage、Scan api of development """

    return redirect(reverse('resources:apiall'))


def lcr(obj, num, flag):
    if 'a' == flag:
        return [obj[i].data for i in xrange(len(obj)) if i % 3 == num]
    else:
        return [obj[i].api.data for i in xrange(len(obj)) if i % 3 == num]


def lcrdict(obj, flag):
    return {'left': lcr(obj, 0, flag), 'center': lcr(obj, 1, flag), 'right': lcr(obj, 2, flag)}


def apirecord(request, p=1):
    status = False
    user = getUI(getUsr(request))

    if request.method == 'GET':
        form = ApiModelForm()
    else:
        form = ApiModelForm(request.POST, request=request)
        if form.is_valid():
            cleaned_data = form.cleaned_data

            api = cleaned_data['api']
            func = cleaned_data['func']
            tag = cleaned_data['tag']
            url = cleaned_data['url']

            a, created = ApiInfo.objects.get_or_create(api=api, func=func, tag=tag, url=url)
            if created:
                a.author = user
                a.save()
                UserApiInfo.objects.create(api=a, user=user)
            else:
                UserApiInfo.objects.create(api=a, user=user, status=False)

            form = ApiModelForm()
            status = True

    mineapi = UserApiInfo.objects.filter(user=user, api__display=True).order_by('-create_time')
    api = pages(mineapi, int(p))

    return render(
        request,
        'resources/api/record.html',
        dict(lcrdict(api.object_list, 'ua'), pages=api, next_url='resources:apimine', form=form, status=status, **getApiDict(request))
    )


@tt_login_required
def apimine(request, p=1):
    mineapi = UserApiInfo.objects.filter(user=getUI(getUsr(request)), api__display=True).order_by('-create_time')
    api = pages(mineapi, int(p))
    return render(
        request,
        'resources/api/mine.html',
        dict(lcrdict(api.object_list, 'ua'), pages=api, next_url='resources:apimine', **getApiDict(request))
    )


def apiall(request, p=1):
    allapi = ApiInfo.objects.filter(display=True).order_by('-create_time')
    api = pages(allapi, int(p))
    return render(
        request,
        'resources/api/all.html',
        dict(lcrdict(api.object_list, 'a'), pages=api, next_url='resources:apiall', **getApiDict(request))
    )


def apisearch(request, p=1):
    _query = request.GET.get('query', '')
    searchapi = ApiInfo.objects.filter(Q(api__contains=_query) | Q(func__contains=_query) | Q(tag__contains=_query) | Q(url__contains=_query), display=True).order_by('-create_time')
    if searchapi.count():
        api = pages(searchapi, int(p))
        return render(
            request,
            'resources/api/search.html',
            dict(lcrdict(api.object_list, 'a'), pages=api, next_url='resources:apisearch', query='?query=' + _query, **getApiDict(request))
        )
    else:
        return HttpResponseRedirect(settings.GOOGLE_SEARCH + _query)


def apidiscuss(request, aid):
    api = ApiInfo.objects.get(pk=aid, display=True).data
    return render(
        request,
        'resources/api/discuss.html',
        dict(api=api, **getApiDict(request))
    )


def softwarehome(request):
    """ Function Software's home - A Navigation Site for IT """

    return render(request, 'resources/resources.html', getResourcesDict(request))