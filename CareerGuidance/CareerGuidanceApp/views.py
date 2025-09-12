from django.http import HttpResponse
from django.shortcuts import render
from django.views import View

from CareerGuidanceApp.forms import HRForm, JobForm
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
                return render(request,'HR/HRhomepage.html')
                              
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
    
class AdminhomepagePage(View):
    def get(self,request):

        return render(request,"Administration/adminhomepage.html")
    
class UserPage(View):
    def get(self,request):
        obj = UserTable.objects.all()
        return render(request,"Administration/view_user.html",{'val': obj})
    
class verifycompanyPage(View):
    def get(self,request):
        obj = HRTable.objects.all()
        return render(request,"Administration/verifycompany.html",{'val': obj})
    
class ApproveCompany(View):
    def post(self, request, login_id):
        obj=LoginTable.objects.get(id=login_id)
        obj.UserType = "hr"
        obj.save()
        return HttpResponse('''<script>alert("Successfully Approved!");window.location="/adminhome";</script>''')


class RejectCompany(View):
    def post(self, request, login_id):
        obj=LoginTable.objects.get(id=login_id)
        obj.UserType = "rejected"
        obj.save()
        return HttpResponse('''<script>alert("Successfully Rejected!");window.location="/adminhome";</script>''')
    
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
    def post(self, request):
        form = JobForm(request.POST)
        print("=================================================", form)
        if form.is_valid():
            f = form.save(commit=False)
            f.save()
            return HttpResponse( '''<script>alert('Job added successfully!');window.location='/addjobPage'</script>''')

    
class hr_registerPage(View):
    def get(self,request):
     return render(request,"HR/hr_register.html")
    def post(self, request):
        form=HRForm(request.POST)
        print("=================================================",form)
        if form.is_valid():
            f=form.save(commit=False)
            f.Login_id=LoginTable.objects.create(Username=f.email_id,Password=request.POST['password'],UserType='pending')
            f.save()
            return HttpResponse(''''<script>alert(' Successfully Registered!');window.location='/LoginPage'</script>''')
       
      
    
    
class managejobPage(View):
    def get(self, request):
        obj = Manage_Job.objects.all()
        return render(request, "HR/managejob.html", {'val': obj})
      
class Hrhomepage(View):
    def get(self,request):
     return render(request,"HR/HRhomepage.html")
    
class applieduserPage(View):
    def get(self,request):
        obj = Job_applied_users.objects.all()
        return render(request,"HR/viewapplieduser.html",{'val': obj})
    
class userPage(View):
    def get(self,request):
        obj = UserTable.objects.all()
        return render(request,"HR/viewuser.html",{'val': obj})
    
    
    