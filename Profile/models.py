from django.db import models

# Create your models here.
# class Team(models.Model):
#     linkedin=models.URLField()
#     github=models.URLField()
    #resume=models.FileField(upload_to='uploads/')
    #pload = models.FileField(upload_to='uploads/

# class Mail_form(models.Model):
#     email=models.EmailField(max_length=254)
#     subject=models.CharField(max_length=254)
#     body=models.CharField(max_length=254)
#
#
#     def __str__(self):
#         return self.subject
# class Profile_About(models.Model):
#     title=models.CharField(max_length=254)
#     summary=models.CharField(max_length=254)
#     def __str__(self):
#         return self.title
# class Projects1(models.Model):
#     job_pic=models.ImageField(upload_to="images/")
#     job_desc=models.CharField(max_length=254)
#     job_tools=models.CharField(max_length=254)
#     def __str__(self):
#         return self.job_desc


House_Type = [
    ('h', 'house,cottage,villa, semi,terrace'),
    ('u', 'duplex'),
    ('t', 'townhouse'),
]
class Team(models.Model):
    pic=models.ImageField(upload_to='Team/')
    name=models.CharField(max_length=100)
    role=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class About_Us(models.Model):
    profile_pic=models.ImageField(upload_to='Team/')
    description=models.CharField(max_length=1000)
    def __str__(self):
        return self.description

class Work_history(models.Model):
    history=models.CharField(max_length=1000)

class Project(models.Model):
    project_img=models.ImageField(upload_to='Team/')
    project_title=models.CharField(max_length=1000)
    project_description=models.CharField(max_length=1000)
    def __str__(self):
        return self.project_title

class Certifictions(models.Model):
    certification_name=models.CharField(max_length=100)

class LinkedIn(models.Model):
    linkedin=models.URLField()
class Github(models.Model):
    github=models.URLField()
class Youtube(models.Model):
    youtube=models.URLField()

class Stack(models.Model):
    stack=models.URLField()

class Contact_model_form(models.Model):
    full_name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    subject=models.CharField(max_length=100)
    message=models.TextField(max_length=10000)
    def __str__(self):
        return self.full_name

class Resume(models.Model):
    title=models.CharField(max_length=100)
    working_company=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    emptype=models.CharField(max_length=100)
    dates=models.CharField(max_length=100)
    def __str__(self):
        return self.title

class Education_data(models.Model):
    degree_name=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    dates=models.CharField(max_length=100)
    def __str__(self):
        return self.degree_name

class Download_Resume(models.Model):
    resume_pdf=models.FileField(upload_to='resume/')

class Deployed_data(models.Model):
    rooms=models.IntegerField(default=0)
    House_Type =models.CharField(max_length=100,choices=House_Type,default="select housetype")
    number_of_bedrooms = models.IntegerField(default=0)
    bathrooms = models.IntegerField(default=0)
    number_of_car_spots = models.IntegerField(default=0)
    landsize = models.FloatField(default=0.0)
    building_area=models.FloatField(default=0.0)

class Pickle(models.Model):
    pickle_file=models.FileField(upload_to="naga/")

class Text_speech_model(models.Model):
    text=models.TextField(max_length=10000)