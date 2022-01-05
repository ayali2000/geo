from django.http.response import HttpResponse
from django.shortcuts import redirect, render

from poll.forms import Vote
from . models import *

def home(request):
    polls=Poll.objects.all()
    context={'polls':polls}
    return render (request,'poll/home.html',context)


def create(requst):
    form=Vote()
    context={'form':form}
    if requst.method=="POST":
        form=Vote(requst.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form=Vote()
    return render(requst,'poll/create.html',context)


def vote(request,pk):
    votes=Poll.objects.get(pk=pk)
    context={'votes':votes}
    if request.method== 'POST':
        select=request.POST['inlineRadioOptions']
        if select == 'option1':
            votes.count_1 += int(1)
        elif select=='option2':
            votes.count_2 += int(1) 
        else:
            return HttpResponse('Invalid form')
                    
        votes.save()  
        return redirect('home')    
    return render(request,'poll/vote.html',context)  


def results(request,pk):
    result=Poll.objects.get(pk=pk)
    context={'result':result}
    return render(request,'poll/result.html',context)          
# Create your views here.
