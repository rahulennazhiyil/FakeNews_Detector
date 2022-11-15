from django.shortcuts import redirect, render

from public.models import *
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse,Http404
from django.urls import reverse
from django.contrib import messages
from .forms import *
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.db.models import Q

from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.
def index(request):
    return render(request,'index.html',)

def register(request):
    if request.method=='POST':
        user_form=UserForm(request.POST)
        profile_form=ProfileForm(request.POST,request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user=user_form.save()
            user.save()

            profile=profile_form.save(commit=False)
            profile.user=user
            profile.save()
            messages.success(request,'Thank You For Registering')
            return redirect('index')

        else:
            HttpResponse('invalid form')
    else:
        user_form=UserForm()
        profile_form=ProfileForm()
       
    return render(request,'account/register.html',{'user_form':user_form,'profile_form':profile_form})

def signin(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('dashboard')
            else:
                return HttpResponse('not active')
        else:
            messages.error(request,'invalid username or password')
            return redirect('signin')
    else:
        return render(request, 'account/signin.html', {})
    


def signout(request):
    logout(request)
    return HttpResponseRedirect('/')




def change_password(request):
    if request.method=="POST":
        form=PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            user=form.save()
            update_session_auth_hash(request,user)
            messages.success(request,"YOUR PASSWORD SUCCEFULLY UPDATED")
            return render(request,'account/change_password.html')
        else:
            messages.error(request,'PLEASE CORRECT ERROR')
    else:
        form=PasswordChangeForm(request.user)
    return render(request,'account/change_password.html',{'form':form})


def update_profile(request):

    if request.method=="POST":
        update_form=UpdateForm(request.POST,instance=request.user)
        update_profile_form=UpdateProfileForm(request.POST,request.FILES,instance=request.user.register)
        if update_form.is_valid() and update_profile_form.is_valid():
            update_form.save()
            update_profile_form.save()
            messages.success(request,f'Your Account has been Updated')
            return redirect('update_profile')
    else:
        update_form=UpdateForm(instance=request.user)
        update_profile_form=UpdateProfileForm(instance=request.user.register)
    context={
        'u_form':update_form,
        'p_form':update_profile_form
    }
    return render(request,'account/profile.html',context)


def dashboard(request):
    
    return render(request,'dashboard/dashboard.html')




