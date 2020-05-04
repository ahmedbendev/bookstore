from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserForm, UserUpdateForm, ProfileUpdateForm,ClientinfoUpdateForm,ProfileForm
from .models import Profile ,Client
def register(request):
    if request.method=='POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            profile = Profile.objects.get(user=user)
            profile.save()
            if profile.type == "client":
               client = Client.objects.create(profile=profile)
               client.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'your account has been created! you are now readu to login !')
            return redirect('profile')
    else:
        form = UserForm()
    return render(request, 'users/register.html',{'form':form})

@login_required
def profile(request):

    u_form= UserUpdateForm(request.POST,request.FILES,instance=request.user)
    p_form= ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
    i_form = ClientinfoUpdateForm(request.POST,request.FILES,instance=request.user.profile.client)
    if request.method=='POST':
        u_form= UserUpdateForm(request.POST,request.FILES,instance=request.user)
        p_form= ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        i_form = ClientinfoUpdateForm(request.POST,request.FILES,instance=request.user.profile.client)
        if u_form.is_valid() and  p_form.is_valid() and i_form.is_valid():
              u_form.save()
              p_form.save()
              i_form.save()
        messages.success(request, f'your profile has been Updated!')
        return redirect('profile')
    else:
        u_form= UserUpdateForm(instance=request.user)
        p_form= ProfileUpdateForm(instance=request.user.profile)
        i_form = ClientinfoUpdateForm(instance=request.user.profile.client)
    context ={
       'u_form' : u_form,
       'p_form' : p_form,
       'i_form' : i_form
    }
    return render(request, 'users/profile.html', context)
