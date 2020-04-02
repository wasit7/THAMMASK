from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from .forms import *
import datetime
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.urls import reverse

# Create your views here.
def index(request):
    if request.user.is_anonymous:
        donate_history = Donate.objects.all()
        return render(request, 'index.html', {'donate_history':donate_history})
    else:
        return redirect('donate:check_user_exists')

@login_required
def home(request):
    return render(request, 'home.html')

@login_required
def verify_user(request):
    profile = Profile.objects.filter(user=request.user)
    if profile.exists():
        return redirect('donate:home')
    else:
        return redirect('donate:profile')

@login_required
def profile(request):
    if request.method == 'POST':
        post_copy = request.POST.copy()
        post_copy['user'] = request.user.pk
        print(post_copy)
        profile = Profile.objects.filter(user=request.user)
        if profile.exists():
            form = ProfileForm(post_copy, instance=Profile.objects.get(user=request.user))
        else:
            form = ProfileForm(post_copy)

        if form.is_valid():
            form.save()
            return redirect('donate:home')
        else:
            data = dict()
            data['nav'] = ({
            '0': [
                    {
                        'page':"ประวัติส่วนตัว",
                        'url':reverse('donate:profile')
                    }
                ]
            })
            
            return render(request, 'settings_up.html', {'data':data})
    else:
        profile = Profile.objects.filter(user=request.user)
        data = dict()
        if profile.exists():
            data['profile'] = Profile.objects.get(user=request.user)
        else:
            data['profile'] = ''
        
        data['nav'] = ({
            '0': [
                {
                    'page':"ประวัติส่วนตัว",
                    'url':reverse('donate:profile')
                }
            ]
        })
        return render(request, 'settings_up.html', {'data':data})

@login_required
def donate(request):
    donator = Profile.objects.get(user__id=request.user.pk)
    if request.method == 'POST':
        post_copy = request.POST.copy()
        post_copy['donator'] = donator
        form = DonateForm(post_copy)
        if form.is_valid():
            form.save()
            return redirect('donate:donate')
    else:
        data = dict()
        data['items'] = DonateItem.objects.filter(show_item=True)
        data['donate'] = Donate.objects.filter(donator=donator).order_by('-id')
        data['nav'] = ({
            '0': [
                {
                    'page':"บริจาค",
                    'url':reverse('donate:donate')
                }
            ]
        })
        data['profile'] = donator
        return render(request, 'donate.html', {'data':data})

@login_required
def request(request):
    receiver = Profile.objects.get(user__id=request.user.pk)
    if request.method == 'POST':
        post_copy = request.POST.copy()
        post_copy['receiver'] = receiver
        form = ReceiveForm(post_copy)
        jobs = Job.objects.all()
        if form.is_valid():
            form.save()
            return redirect('donate:request')
    else:
        data = dict()
        data['items'] = Item.objects.all()
        data['receive'] = Receive.objects.filter(receiver=receiver).order_by('-id')
        data['nav'] = ({
            '0': [
                {
                    'page':"ขอรับบริจาค",
                    'url':reverse('donate:request')
                }
            ]
        })
        data['jobs'] = Job.objects.all()
        data['profile'] = receiver
        data['hospitals'] = Hospital.objects.all()
        return render(request, 'request.html', {'data':data})

@login_required
def review(request):
    return render(request, 'review.html')