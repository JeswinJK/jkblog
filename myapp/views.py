from django.shortcuts import render,redirect
from .forms import newuserform
def home(request):
    return render(request,'home.html')
def must(request):
    return render(request,'must.html')
def food(request):
    return render(request,'food.html')
def register(request):
    if request.method=="POST":
        form=newuserform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    form=newuserform()
    return render(request,'register.html',{'form':form})

# Create your views here.
