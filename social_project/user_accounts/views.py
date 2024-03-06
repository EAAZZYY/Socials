from django.shortcuts import render,redirect
from .forms import RegisterForm,ProfileForm
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.

def register(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
            
    else:
        form = RegisterForm
        context = {"form":form}
    return render(request,'user_accounts/register.html',context)

@login_required
def profile(request,id):
    profile = Profile.objects.get(id=id)
    return render(request, 'user_accounts/profile.html',{"profile":profile})


@login_required
def profile_edit(request):
    if request.method == "POST":
        form = ProfileForm(data=request.POST, files=request.FILES, instance=request.user.profile)
        
        if form.is_valid():
            form.save()
            return redirect("index")
    
    else:
        form = ProfileForm(instance=request.user.profile,files=request.FILES)
    return render(request, "user_accounts/profile_form.html", {"form":form}) 


@login_required
def index(request):
    return render(request,"user_accounts/index.html")