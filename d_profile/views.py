from django.shortcuts import render,redirect,get_object_or_404
from django.http import Http404
from django.urls import reverse
from .form import EditProfile
from .models import Profile
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def profile_page(request,username=None):
    try:
        if username:
            profile = get_object_or_404(User,username=username).profile
        else:
            profile = request.user.profile    
    except:
            raise Http404()
    return render(request,"d_profile/profile.html",{
        "profile":profile
    })

@login_required
def edit_profile(request):
    user = request.user
    profile,created = Profile.objects.get_or_create(user=user)
    form = EditProfile(instance=profile)
    if request.method == 'POST':
        form = EditProfile(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request,'Profile updated successfully')
            return redirect('profile_page')
    if request.path == reverse('profile_onboarding'):
        template = "d_profile/complet_profile.html"
    else:
        template = "d_profile/edit_profile.html"    

    return render(request,template,{
        "form":form
    })

@login_required
def delete_profile(request):
    user = request.user
    if request.method == 'POST':
        logout(request)
        user.delete()
        messages.success(request,'Account deleted successfully, what a pity')
        return redirect('homepage')
    return render(request,'d_profile/del_profile.html')
    