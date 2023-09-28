from django.shortcuts import render,redirect
from .models import Download_Resume,About_Us,Team,Work_history,Project,Certifictions,LinkedIn,Youtube,Github,Stack,Resume,Education_data,Pickle
from .forms import contact_form,Deploy_form,Text_to_speech_from
from django.core.mail import BadHeaderError,send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
import pickle
# from joblib import load
from sklearn.preprocessing import StandardScaler,LabelEncoder
from IPython.display import Audio,display
from gtts import gTTS
from tempfile import TemporaryFile


# Create your views here.
def home(request):
    # profile = Profile_About.objects.get(id=1)
    # all_jobs = Projects1.objects.all()
    # return render(request,'profile/home1.html',{"profile":profile,"all_jobs":all_jobs})
    down_resume=Download_Resume.objects.get(id=1)
    education=Education_data.objects.all()
    resume=Resume.objects.all()
    team_data=Team.objects.all()
    work_data=Work_history.objects.all()
    about_us=About_Us.objects.get(id=1)
    certifications=Certifictions.objects.all()
    projects=Project.objects.all()[::-1]
    form = contact_form()
    return render(request, 'profile/home1.html',{"projects":projects,"down_resume":down_resume,"education":education,"resume":resume,"contact_form":form,"team_data":team_data,"work_data":work_data,"about_us":about_us,"certifications":certifications})




def home1(request):
    if request.method=="POST":
        filled_form=contact_form(request.POST)
        if filled_form.is_valid():
            filled_full_name=filled_form.cleaned_data["full_name"]
            filled_email=filled_form.cleaned_data["email"]
            filled_subject=filled_form.cleaned_data["subject"]
            filled_message=filled_form.cleaned_data["message"]

            from_email_user="nagababuupputuri52@gmail.com"
            receiver="nagababuupputuri@gmail.com"
            subject="Your Portfolio subject +' ' +{}".format(filled_subject)
            website_messages="You are Received mail from {} with this {} sent by {}  information was  {}".format(filled_email,filled_subject,filled_full_name,filled_message)

            status=send_mail(subject,website_messages,from_email_user,[receiver])
            if status:
                filled_form.save()
            else:
                pass
                # messages.success(request,"Your request Stored , will reach you asap")
            return redirect("home")



def Price_Prediction(request):
    if request.method == "POST":
        filled_form = form = Deploy_form(request.POST)
        if filled_form.is_valid():
            # retrive data  from the form
            rooms = filled_form.cleaned_data["rooms"]
            house_type = filled_form.cleaned_data["House_Type"]
            no_of_bedrooms = filled_form.cleaned_data["number_of_bedrooms"]
            bathrooms = filled_form.cleaned_data["bathrooms"]
            no_of_car_spots = filled_form.cleaned_data["number_of_car_spots"]
            landsize = filled_form.cleaned_data["landsize"]
            building_area = filled_form.cleaned_data["building_area"]

            all_data = Pickle.objects.all()[0].pickle_file.name
            file = open(all_data, "rb")
            test = pickle.load(file)
            h_types = {"h": 0, "u": 1, 't': 2}
            scaler = StandardScaler()
            price = "The Price of the House is {}".format(
                "%.2f" % test.predict(
                    [[rooms, h_types[house_type], no_of_bedrooms, bathrooms, no_of_car_spots, landsize, building_area]])
            )
            form = Deploy_form()
            return render(request, "profile/HousePrediction.html", {"cost": price, "pre_form": form})


    form = Deploy_form()
    return render(request, 'profile/HousePrediction.html', {"pre_form": form})


c=0
def TextToSpeech(request):
    if request.method=="POST":
        global c
        filled_form=Text_to_speech_from(request.POST)
        if filled_form.is_valid():
            text_data=filled_form.cleaned_data["text"]
            if c%2==0:  ##first time
                tts = gTTS(text=text_data, lang='en')
            else:
                tts = gTTS(text=text_data, lang='en',slow=True)
            f = TemporaryFile()
            tts.write_to_fp(f)
            f.seek(0)
            audio = Audio(f.read(), autoplay=True)
            # f.close()
            src_data=audio.src_attr()

            c+=1
            form=Text_to_speech_from({"text":text_data})
            print("This is a ",c)
            return  render(request,'profile/text.html',{"form":form,"aud":src_data})
    c=0
    form=Text_to_speech_from()
    return render(request,'profile/text.html',{"form":form})

def linkedin(request):
    link_data=LinkedIn.objects.get(id=1)
    # return  render(request,"profile/home1.html",{"linkedin_data":link_data})
    return redirect(link_data.linkedin)

    # return redirect(link_data.linkedin)
def github(request):
    git_data = Github.objects.get(id=1)
    return redirect(git_data.github)
    # return render(request,"profile/home1.html",{"git_data":git_data})
def youtube(request):
     you_data = Youtube.objects.get(id=1)
     return  redirect(you_data.youtube)
     # return  render(request,'profile/home1.html',{"resume_data":resume_data})


def stack(request):
    stack_data = Stack.objects.get(id=1)
    return  redirect(stack_data.stack)
    # return render(request, 'profile/home1.html', {"stack_data": stack_data})
