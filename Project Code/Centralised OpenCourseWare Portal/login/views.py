# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import logout_then_login
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages
from django.contrib.auth.models import User

from login.forms import UserForm,MyUserForm
from login.models import Users

def signup_view(request):
    dict = {}
    form1 = UserForm()
    form2 = MyUserForm()
    if request.POST:
        form1 = UserForm(request.POST)
        form2 = MyUserForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            data = form1.cleaned_data
            form1.save()
            obj=form2.save(commit=False)
            obj.user=User.objects.get(username = data['username'])
            obj.save()
            form2.save_m2m()
            messages.add_message(request, messages.INFO, " You have successfully registered. You can sign in now.")
            return (redirect(reverse('home')))
    dict['form1'] = form1
    dict['form2'] = form2
    return render_to_response('signup.html',dict,context_instance=RequestContext(request))

def login_view(request):
    state="please login"
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request,user)
                response = redirect(reverse('home'))
                return(response)
            else:
                state = "Your account is not active, please contact the admin"
        else:
            state = "Your username and/or password were incorrect"
    messages.add_message(request, messages.ERROR, state)
    return render_to_response('homepage.html',context_instance=RequestContext(request))

def logout_view(request):
    return logout_then_login(request,login_url='/')