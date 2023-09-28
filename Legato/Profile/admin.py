from django.contrib import admin
from .models import  Text_speech_model,Download_Resume,Education_data,Resume,Work_history,About_Us,Stack,Certifictions,LinkedIn,Contact_model_form,Youtube,Github,Project,Team,Deployed_data,Pickle
# # Register your models here.
admin.site.register(Work_history)
admin.site.register(About_Us)
admin.site.register(Stack)
admin.site.register(Certifictions)
admin.site.register(LinkedIn)
admin.site.register(Contact_model_form)
admin.site.register(Youtube)
admin.site.register(Github)
admin.site.register(Project)
admin.site.register(Team)
admin.site.register(Resume)
admin.site.register(Education_data)
admin.site.register(Download_Resume)
admin.site.register(Deployed_data)
admin.site.register(Pickle)
admin.site.register(Text_speech_model)