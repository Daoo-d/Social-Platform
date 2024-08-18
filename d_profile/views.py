from django.shortcuts import render,redirect
from .form import EditProfile
from .models import Profile

# Create your views here.
def profile_page(request):
    user = request.user
    profile,created = Profile.objects.get_or_create(user=user)
    return render(request,"d_profile/profile.html",{
        "profile":profile
    })

def edit_profile(request):
    user = request.user
    profile,created = Profile.objects.get_or_create(user=user)
    form = EditProfile(instance=profile)
    if request.method == 'POST':
        form = EditProfile(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_page')
    return render(request,"d_profile/edit_profile.html",{
        "form":form
    })