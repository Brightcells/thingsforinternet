# -*- coding: utf-8 -*-

from django.conf import settings
from django.core.paginator import Paginator
from django.core.urlresolvers import reverse
from django.db.models import Q
from django.forms.models import model_to_dict
from django.shortcuts import redirect, render

from huntjob.forms import QuestionInfoModelForm
from huntjob.models import QuestionInfo
from thingsforinternet.decorators import tt_login_required
from utils.tt4it_utils import *


HUNTJOBBACKLINKS = [
    {'name': 'TT4IT', 'url': 'dh:dh', 'para': ''},
    {'name': '求职', 'url': 'huntjob:huntjob', 'para': ''},
]
QUESTIONBACKLINKS = HUNTJOBBACKLINKS + [{'name': '面试题', 'url': 'huntjob:questionhome', 'para': ''}]


def pages(setlist, p):
    """ Paginator """

    paginator = Paginator(setlist, settings.TIPS_PER_PAGE)
    try:
        return paginator.page(p)
    except Exception:
        return paginator.page(1)


def getHuntjobDict(request):
    usr, ui = getUsrUI(request)
    display_bg, slide_image_classify = (ui.display_bg, ui.classify) if ui else (True, '')

    return {
        'backlinks': HUNTJOBBACKLINKS,
        'lists': getFunc(request, 'huntjob'),
        'usr': usr,
        'display_bg': display_bg,
        'slide_image_classify': slide_image_classify
    }


def getQuestionDict(request):
    usr, ui = getUsrUI(request)
    display_bg, slide_image_classify = (ui.display_bg, ui.classify) if ui else (True, '')

    return {
        'backlinks': QUESTIONBACKLINKS,
        'lists': getNav(request, 'question'),
        'usr': usr,
        'display_bg': display_bg,
        'slide_image_classify': slide_image_classify
    }


def huntjob(request):
    """ APP Huntjob's home """

    return render(request, 'huntjob/huntjob.html', getHuntjobDict(request))


def questionhome(request):
    """ Function Question's home - Upload、Manage、Scan interview questions """

    return redirect(reverse('huntjob:questionall'))


@tt_login_required
def questionrecord(request, p=1):
    status = False
    user = getUI(getUsr(request))

    if request.method == 'GET':
        form = QuestionInfoModelForm()
    else:
        form = QuestionInfoModelForm(request.POST, request=request)
        if form.is_valid():
            cleaned_data = form.cleaned_data

            question = cleaned_data['question']
            answer = cleaned_data['answer']
            tag = cleaned_data['tag']

            QuestionInfo.objects.get_or_create(question=question, answer=answer, tag=tag, user=user)

            form = QuestionInfoModelForm()
            status = True

    minequestion = QuestionInfo.objects.filter(user=getUI(getUsr(request)), display=True).order_by('-modify_time')
    questions = pages(minequestion, int(p))
    minequestion = [question.data for question in questions.object_list]

    return render(
        request,
        'huntjob/question/record.html',
        dict(blog=minequestion, pages=questions, next_url='huntjob:questionmine', form=form, status=status, **getQuestionDict(request))
    )


def questionall(request, p=1):
    allquestion = QuestionInfo.objects.filter(display=True).order_by('-modify_time')
    questions = pages(allquestion, int(p))
    allquestion = [question.data for question in questions.object_list]
    return render(
        request,
        'huntjob/question/all.html',
        dict(question=allquestion, pages=questions, next_url='huntjob:questionall', **getQuestionDict(request))
    )


@tt_login_required
def questionmine(request, p=1):
    minequestion = QuestionInfo.objects.filter(user=getUI(getUsr(request)), display=True).order_by('-modify_time')
    questions = pages(minequestion, int(p))
    minequestion = [question.data for question in questions.object_list]

    return render(
        request,
        'huntjob/question/mine.html',
        dict(question=minequestion, pages=questions, next_url='huntjob:questionmine', **getQuestionDict(request))
    )


@tt_login_required
def questionedit(request):
    if request.method == 'POST':
        minequestion, created = QuestionInfo.objects.get_or_create(user=getUI(getUsr(request)), display=True)
        form = QuestionInfoModelForm(request.POST, request.FILES, instance=minequestion)
        if form.is_valid():
            form.save()

    try:
        minequestion = model_to_dict(QuestionInfo.objects.get(user=getUI(getUsr(request)), display=True))
        form = QuestionInfoModelForm(minequestion)
    except Exception:
        form = QuestionInfoModelForm()

    return render(
        request,
        'huntjob/question/edit.html',
        dict(form=form, userinfo=getUI(getUsr(request)), **getQuestionDict(request))
    )


def questiondiscuss(request, qid):
    try:
        question = QuestionInfo.objects.get(pk=qid, display=True)
    except QuestionInfo.DoesNotExist:
        question = None

    userinfo = question.user.data if question else None
    question = question.data if question else {}

    return render(
        request,
        'huntjob/question/discuss.html',
        dict(question=question, userinfo=userinfo, **getQuestionDict(request))
    )


def questionsearch(request, p=1):
    _query = request.GET.get('query', '')
    searchquestion = QuestionInfo.objects.filter(Q(question__contains=_query) | Q(answer__contains=_query) | Q(tag__contains=_query), display=True).order_by('-modify_time')
    questions = pages(searchquestion, int(p))
    searchquestion = [question.data for question in questions.object_list]
    return render(
        request,
        'huntjob/question/search.html',
        dict(question=searchquestion, pages=questions, next_url='huntjob:questionsearch', query='?query=' + _query, **getQuestionDict(request))
    )
