"""Legato URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Profile import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('home1/',views.home1,name='home1'),
    path('linkedin/',views.linkedin,name="linkedin"),
    path('Github/',views.github,name="github"),
    path('youtube/',views.youtube,name="youtube"),
    path('stackoverflow/',views.stack,name='stack'),
    path('price-prediction/',views.Price_Prediction,name='price_predict'),
    path('text-to-speech/',views.TextToSpeech,name='tx_to_sp'),
    #path('',views.linkedin,name="linkedin"),
    #path('Resume/',views.resume,name="resume"),
    # path('Mail/',views.Mail,name="mail"),
    #path("jobs/",views.jobs,name="jobs"),
    #path('job/<int:pk_id>/',views.job_data,name="job_data"),
    # path('Project/<int:pro_id>/',views.Project_details1,name="Project_detail1"),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

