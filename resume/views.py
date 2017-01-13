# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render

from resume.forms import ResumeInfoModelForm
from resume.models import ResumeInfo
from thingsforinternet.decorators import tt_login_required
from utils.tt4it_utils import *


RESUMEBACKLINKS = [
    {'name': 'TT4IT', 'url': 'dh:dh', 'para': ''},
    {'name': '简历', 'url': 'resume:resume', 'para': ''},
]
RESUME2BACKLINKS = RESUMEBACKLINKS + [{'name': '简历', 'url': 'resume:resume2home', 'para': ''}]


def pages(setlist, p):
    """ Paginator """

    paginator = Paginator(setlist, settings.TIPS_PER_PAGE)
    try:
        return paginator.page(p)
    except:
        return paginator.page(1)


def getResumeDict(request):
    usr, ui = getUsrUI(request)
    display_bg, slide_image_classify = (ui.display_bg, ui.classify) if ui else (True, '')

    return {
        'backlinks': RESUMEBACKLINKS,
        'lists': getFunc(request, 'resume'),
        'usr': usr,
        'display_bg': display_bg,
        'slide_image_classify': slide_image_classify
    }


def getResume2Dict(request):
    usr, ui = getUsrUI(request)
    display_bg, slide_image_classify = (ui.display_bg, ui.classify) if ui else (True, '')

    return {
        'backlinks': RESUME2BACKLINKS,
        'lists': getNav(request, 'resume2'),
        'usr': usr,
        'display_bg': display_bg,
        'slide_image_classify': slide_image_classify
    }


def resume(request):
    """ APP Resume's home """

    return render(request, 'resume/resume.html', getResumeDict(request))


def resume2home(request):
    """ Function Resume2's home - Upload、Manage、Scan resume of development """

    return redirect(reverse('resume:resume2all'))


def resume2all(request, p=1):
    allresume = ResumeInfo.objects.filter(display=True).order_by('-modify_time')
    resumes = pages(allresume, int(p))
    allresume = [resume.info for resume in resumes.object_list]
    return render(
        request,
        'resume/resume2/all.html',
        dict(resume=allresume, pages=resumes, next_url='resume:resume2all', **getResume2Dict(request))
    )


@tt_login_required
def resume2mine(request):
    ui = getUI(getUsr(request))
    try:
        mineresume = ResumeInfo.objects.get(user=ui, display=True).data
    except:
        mineresume = {}
    return render(
        request,
        'resume/resume2/mine_editormd.html',
        dict(resume=mineresume, ui=ui, userinfo=ui.data, **getResume2Dict(request))
    )


@tt_login_required
def resume2edit(request):
    if request.method == "POST":
        mineresume, created = ResumeInfo.objects.get_or_create(user=getUI(getUsr(request)), display=True)
        form = ResumeInfoModelForm(request.POST, request.FILES, instance=mineresume)
        if form.is_valid():
            form.save()

        return redirect(reverse('resume:resume2mine'))

    try:
        mineresume = model_to_dict(ResumeInfo.objects.get(user=getUI(getUsr(request)), display=True))
        form = ResumeInfoModelForm(mineresume)
    except:
        form = ResumeInfoModelForm()

    return render(
        request,
        'resume/resume2/edit_editormd.html',
        dict(form=form, userinfo=getUI(getUsr(request)), **getResume2Dict(request))
    )


def resume2discuss(request, uid):
    try:
        resume = ResumeInfo.objects.get(user__pk=uid, display=True)
    except:
        resume = None

    userinfo = resume.user.data if resume else None
    resume = resume.data if resume else {}

    return render(
        request,
        'resume/resume2/discuss_editormd.html',
        dict(resume=resume, userinfo=userinfo, **getResume2Dict(request))
    )


def resume2discuss2(request, uid):
    try:
        resume = ResumeInfo.objects.get(user__pk=uid, display=True)
    except:
        resume = None

    userinfo = resume.user.data if resume else None
    resume = resume.data if resume else {}

    return render(
        request,
        'resume/resume2/discuss2.html',
        dict(resume=resume, userinfo=userinfo, **getResume2Dict(request))
    )


def resume2search(request, p=1):
    _query = request.GET.get('query', '')
    searchresume = ResumeInfo.objects.filter(Q(resume__contains=_query) | Q(tag__contains=_query), display=True).order_by('-modify_time')
    resumes = pages(searchresume, int(p))
    searchresume = [resume.info for c in resumes.object_list]
    return render(
        request,
        'resume/resume2/search.html',
        dict(resume=searchresume, pages=resumes, next_url='resume:resume2search', query='?query=' + _query, **getResume2Dict(request))
    )
