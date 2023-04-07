from django.shortcuts import render,redirect
from .registerform import userRegisterForm,Userupdateform,Profileupdateform
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile
# Create your views here.

def register(request):
    if request.method=='POST':
        form=userRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Your Account has benn created! You are now able to Log In')
            return redirect('login')
    else:
        form=userRegisterForm()

    return render(request,'register/userform.html',{'form':form})   

@login_required
def profile(request):
   
    if request.method=='POST':
     u_form=Userupdateform(request.POST,instance=request.user)
     
     
     if u_form.is_valid:
        u_form.save()
        messages.success(request,f'Your Account has been updated!')
        return redirect('form_home')
    else:
     u_form=Userupdateform(instance=request.user)
     
    context={
        'u_form':u_form,
        
    }

    return render(request,'register/profile.html',context)


       