from django.contrib import admin
from .models import TF_Question, MC_Question, SA_Question, FB_Question, Assignment

admin.site.register(TF_Question)
admin.site.register(MC_Question)
admin.site.register(SA_Question)
admin.site.register(FB_Question)
admin.site.register(Assignment)
