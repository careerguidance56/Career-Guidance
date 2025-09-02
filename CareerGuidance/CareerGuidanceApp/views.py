from django.shortcuts import render
from django.views import View

from CareerGuidanceApp.models import *
# Create your views here.
class LoginPage(View):
    def get(self, request):
        return render(request, "Administration/login.html")
    
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        try:
            user=LoginTable.objects.get(Username=username,Password=password)
            request.session['login_id'] = user.id
            if user.UserType=='admin':
                return render(request,'Administration/homepage.html')
            elif user.UserType=='HR':
                return render(request,'HR/homepage.html')
                              
        except LoginTable.DoesNotExist:
            return render(request,'"---------',{'error':'Invalid username or password'})
        


# ///////////////////////////////////////////////////////// Administration /////////////////////////////////////////////

class addcoursePage(View):
    def get(self,request):
      
        return render(request,"Administration/add_course.html",)
class certificatePage(View):
    def get(self,request):

        return render(request,"Administration/certificate.html")
    
class addCertificatePage(View):
    def get(self,request):
        return render(request,"Administration/add_certificate.html")
    
class loginPage(View):
    def get(self,request):

        return render(request,"Administration/login.html")
    
class homepagePage(View):
    def get(self,request):

        return render(request,"Administration/homepage.html")
    
class UserPage(View):
    def get(self,request):
        obj = UserTable.objects.all()
        return render(request,"Administration/view_user.html",{'val': obj})
    
class verifycompanyPage(View):
    def get(self,request):
        obj = Manage_Job.objects.all()
        return render(request,"Administration/verifycompany.html",{'val': obj})
    
class viewcoursePage(View):
    def get(self,request):

        return render(request,"Administration/viewcourse.html")
    
class viewfeedbackPage(View):
    def get(self,request):
        obj = Feedback.objects.all()
        return render(request,"Administration/viewfeedback.html",{'val': obj})
       
# ////////////////////////////////////////////// HR //////////////////////////////////////////   

class addjobPage(View):
    def get(self,request):

        return render(request,"HR/addjob.html")
    
class hr_registerPage(View):
    def get(self,request):

        return render(request,"HR/hr_register.html")
    
class managejobPage(View):
    def get(self,request):

        return render(request,"HR/managejob.html")
    
class homepage(View):
    def get(self,request):

        return render(request,"HR/page.html")
    
class applieduserPage(View):
    def get(self,request):

        return render(request,"HR/viewapplieduser.html")
    
class userPage(View):
    def get(self,request):

        return render(request,"HR/viewuser.html")
    
    
    