from django.shortcuts import render,redirect
from .forms import  *

def index(request):
    users=Users.objects.filter(pol='Мужской')
    return render(request,'home.html',{'users':users})

def about(request):
    users=Users.objects.filter(pol='Женский')
    return render(request,'index.html',{'users':users})


def func(request):
    return render(request,'index.html')
def regfunc(request):
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=UserForm()

    return render(request,'reg.html',{ 'form':form })