from django.shortcuts import render,HttpResponse,redirect
from msgapp.models import Msg


# Create your views here.
def creat(request):
    if request.method=='GET':
        return render(request,'create.html')
    else:
        name=request.POST['uname']
        email=request.POST['email']
        mobilenumber=request.POST['mob']
        message=request.POST['msg']

        val=Msg.objects.create(name=name,email=email,mobile=mobilenumber,msg=message)
        val.save()
        return redirect('/dashboard')
def dashboard(request):
    data=Msg.objects.all()
    context={}
    context['data']=data
    return render(request,'dashboard.html',context)

def delete(request,rid):
    data=Msg.objects.filter(id=rid)
    data.delete()
    return redirect('/dashboard')
    
def edit(request,rid):
    if request.method=='GET':
        data=Msg.objects.get(id=rid)
        context={ }
        context['data']=data
        return render(request,'edit.html',context)
    else:
        name=request.POST['uname']
        email=request.POST['email']
        mobilenumber=request.POST['mob']
        message=request.POST['msg']
        data=Msg.objects.filter(id=rid)
        data.delete()
        val=Msg.objects.create(name=name,email=email,mobile=mobilenumber,msg=message)
        val.save()
        return redirect('/dashboard')