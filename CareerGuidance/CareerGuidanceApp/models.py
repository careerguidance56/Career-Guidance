from django.db import models

# Create your models here.
class LoginTable(models.Model):
    Username = models.CharField(max_length=30, blank=True, null=True)
    Password = models.CharField(max_length=30, blank=True, null=True)
    UserType = models.CharField(max_length=30, blank=True, null=True)


class UserTable(models.Model):
   
    Login_id = models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True, null=True)
    name = models.CharField(max_length=30, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)  # Removed max_length
    phone_no = models.BigIntegerField(blank=True, null=True)
    gender = models.CharField(max_length=30, blank=True, null=True)
    email_id = models.CharField(max_length=30, blank=True, null=True)
    Qualification = models.CharField(max_length=30, blank=True, null=True)


class HRTable(models.Model):
  
    Login_id = models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True, null=True)
    Company_name = models.CharField(max_length=30, blank=True, null=True)
    Address = models.CharField(max_length=30, blank=True, null=True)
    phone_no = models.BigIntegerField(blank=True, null=True)
    email_id = models.CharField(max_length=30, blank=True, null=True)

class add_certificate(models.Model):

    Login_id = models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True, null=True)
    file = models.FileField(max_length=30, blank=True, null=True)
   

class jobTable(models.Model):
   
    Login_id = models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True, null=True)
    
    Job_name = models.CharField(max_length=30, blank=True, null=True)
    Job_details = models.CharField(max_length=30, blank=True, null=True)
    Qualification = models.CharField(max_length=30, blank=True, null=True)
    Experience = models.CharField(max_length=30, blank=True, null=True)
    phone_no = models.BigIntegerField(blank=True, null=True)

class Add_course(models.Model):
   
    Course_name = models.CharField(max_length=30, blank=True, null=True)
    Course_details = models.CharField(max_length=30, blank=True, null=True)
    Category = models.CharField(max_length=30, blank=True, null=True)
    Start_date = models.DateField(max_length=30, blank=True, null=True)
    End_date = models.DateField(max_length=30, blank=True, null=True) 

class Feedback(models.Model):

    Login_id = models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True, null=True)
    Feedback = models.CharField(max_length=30, blank=True, null=True)
    Rating = models.IntegerField(blank=True, null=True)

class Job_applied_users(models.Model):
    
    Login_id = models.ForeignKey(UserTable,on_delete=models.CASCADE,blank=True, null=True)
    Job_role = models.CharField(max_length=30, blank=True, null=True)
    Resume = models.FileField(max_length=30, blank=True, null=True)
    Status = models.CharField(max_length=30, blank=True, null=True)

class Upload_resume(models.Model):
  
    Login_id = models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True, null=True)
    Resume = models.FileField(max_length=30, blank=True, null=True)

class enroll_course(models.Model):

    Login_id = models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True, null=True)
    Course_id = models.IntegerField(blank=True, null=True)
    Created_at = models.DateField(max_length=30, blank=True, null=True)

class Take_quiz(models.Model):

    question_id = models.IntegerField(blank=True, null=True)

class Result(models.Model):
   
    Question_id = models.IntegerField(blank=True, null=True)
    User_id = models.IntegerField(blank=True, null=True)
    Result = models.CharField(max_length=30, blank=True, null=True)
    created_at = models.DateField(max_length=30, blank=True, null=True)

class view_and_enroll_course(models.Model):

    login_id = models.ForeignKey(LoginTable,on_delete=models.CASCADE,blank=True, null=True)
    Course_id = models.IntegerField(blank=True, null=True)
    Course_details = models.CharField(max_length=30, blank=True, null=True)
    Category = models.CharField(max_length=30, blank=True, null=True)
    Duration = models.CharField(max_length=30, blank=True, null=True)
  



   


   


   

