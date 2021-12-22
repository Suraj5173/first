from django.shortcuts import redirect, render,HttpResponseRedirect
from .forms import loginform, signupform,postform
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,login
from .models import Post
from django.contrib.auth.models import Group


# Create your views here.

def home(request):
    posts=Post.objects.all()
    return render(request,'home.html',{'posts':posts})



def dashboard(request):
    if request.user.is_authenticated:
     posts=Post.objects.all()
     user=request.user
     full_name=user.get_full_name()
     gps=user.groups.all()
     return render(request,'dashboard.html',{'posts':posts,'full_name':full_name,'groups':gps})
    else:
        return HttpResponseRedirect ('/login/')

def addpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form =postform(request.POST)
            if form.is_valid():
                title=form.cleaned_data['title']
                desc=form.cleaned_data['desc']
                pst=Post(title=title,desc=desc)
                pst.save()
                form=postform()
        else:
            form=postform()    
        return render(request,'addpost.html',{'form':form})
    else:
        return HttpResponseRedirect('/login/')    

def updatepost(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi= Post.objects.get(pk=id)
            form= postform(request.POST,instance=pi)
            if form.is_valid():
                form.save()
        else:
            pi= Post.objects.get(pk=id)
            form= postform(instance=pi)
        return render(request,'updatepost.html',{'form':form})
                    
    else:
        return HttpResponseRedirect('/login/')    

def deletepost(request,id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi= Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dash/')
    else:
        return HttpResponseRedirect('/login/')    



def loginf(request):
    if not request.user.is_authenticated:    
        if request.method == 'POST':
            form = loginform(request = request,data = request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname,password=upass)
                if user is not None:
                    login(request,user)
                    messages.success(request,'logged in successfully')
                    return HttpResponseRedirect('/dash/')
        else:
            form=loginform()
        return render(request,'login.html',{'form':form}) 
    else:
        return HttpResponseRedirect('/dash/')


def signup(request):
    if request.method == 'POST':
        form=signupform(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations Staff is created')
            user=form.save()
            group= Group.objects.get(name='Staff')
            user.groups.add(group)

    else:
        form=signupform()
    return render(request,'signup.html',{'form':form}) 

def logoutf(request):
    logout(request)
    return HttpResponseRedirect('/')           