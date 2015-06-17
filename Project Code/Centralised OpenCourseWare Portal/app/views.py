from django.shortcuts import render, render_to_response, RequestContext
from django.contrib import messages

from app.models import OpenCourse
from login.models import Users
from ratings.models import Score

# Create your views here.

def homepage(request):
    print(Users.objects.filter(user__username=request.user.username).values('is_panel'))
    send_dict = {}
    item = OpenCourse.objects.order_by('-pubDate')[:5].values('title','slug')
    send_dict['lcourses'] = item
    if request.user.is_authenticated:
        list1 = Users.objects.filter(user__username=request.user.username).values_list('interests__category', flat=True)
        for each_interest in list1:
            item = OpenCourse.objects.order_by("-rating").filter(category__category__iexact=each_interest).values('title','slug')
        print("fetch")
        print(item)
        send_dict['course'] = item
    return render_to_response("homepage.html",send_dict, context_instance=RequestContext(request))

def aboutpage(request):
    return render_to_response("aboutpage.html",locals(), context_instance=RequestContext(request))

def t_login(request):
    return render_to_response("tlogin.html",locals(), context_instance=RequestContext(request))
