from django.shortcuts import render, render_to_response, RequestContext, redirect
from django.core.urlresolvers import reverse
from ratings.models import Score

from app.models import OpenCourse
# Create your views here.

def sprovider(request,arg=None):
    send_dict ={}
    try:
        item = OpenCourse.objects.values('provider').distinct()
    except:
        item = []
    send_dict['list'] = item
    if arg:
        try:
            item = OpenCourse.objects.order_by("-rating").filter(provider=arg).values('title','slug')
        except:
            item = []
        send_dict['course'] = item
    return render_to_response('search/provider.html',send_dict, context_instance=RequestContext(request))


def slanguage(request,arg=None):
    send_dict ={}
    try:
        item = OpenCourse.objects.values('language').distinct()
    except:
        item = []
    send_dict['list'] = item
    if arg:
        try:
            item = OpenCourse.objects.filter(language=arg).values('title','slug').order_by("-rating")
        except:
            item = []
        send_dict['course'] = item
    return render_to_response('search/language.html',send_dict, context_instance=RequestContext(request))

def scategory(request,arg=None):
    send_dict ={}
    try:
        item = OpenCourse.objects.values('category__category').distinct()
    except:
        item = []
    send_dict['list'] = item
    if arg:
        try:
            item = OpenCourse.objects.order_by("-rating").filter(category__category__icontains=arg).values('title','slug')
        except:
            item = []
        send_dict['course'] = item
    return render_to_response('search/category.html',send_dict, context_instance=RequestContext(request))

def detail_view(request,slug):
    dict = {}
    try:
        item = OpenCourse.objects.get(slug = slug)
    except:
        item = []
    try:
        score = Score.objects.get(object_id = item.id)
        new_rating = ( (item.panel_rating/2) + (0.75*score.average) )/2  
        item = OpenCourse.objects.filter(slug=slug).update(rating=new_rating)
        item = OpenCourse.objects.get(slug = slug)
    except:
        score=[]
    dict['course'] = item
    return render_to_response('search/course_detail.html',dict,context_instance=RequestContext(request))

def search(request):
    send_dict = {}
    if request.POST:
        try:
            squery = request.POST.get('query')
            item=OpenCourse.objects.order_by("-rating").filter(title__icontains = squery)
        except:
            print("Search Error")
            response = redirect(reverse('home'))
            return(response)
        send_dict['course'] = item
        return render_to_response('search/courses.html',send_dict, context_instance=RequestContext(request))
    return render_to_response('homepage.html',context_instance=RequestContext(request))

