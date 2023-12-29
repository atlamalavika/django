from django.shortcuts import render,redirect
from .models import User1
# Create your views here.
def Registration(request):
    if request.method=='POST':
        rname=request.POST['name']
        remail=request.POST['email']
        rpassword=request.POST['password']
        rconfirmpassword=request.POST['confirmpassword']
                  
        if rpassword!=rconfirmpassword:
            return render(request,'error.html')
        else:
            details=User1(name=rname,email=remail,password=rpassword,confirmpassword=rconfirmpassword)    
            details.save()
            return  redirect(Login1)
    return render(request,'registration.html')       
def Login1(request):
    if request.method=='POST':
        rname=request.POST['name']
        rpassword=request.POST['password']        
        Details=User1.objects.all()     
        for user in Details:            
            if user.name==rname and user.password==rpassword:
                return redirect(Home)            
    return render(request,'login1.html')   
def Home(request):
    if request.method=='POST':
        return redirect(Login1)
    return render(request,'home.html')

   
# def Logout1(request):
#     return redirect(Login1)
