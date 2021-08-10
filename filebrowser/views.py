from django.shortcuts import render
from django.shortcuts import redirect
from user.models import Member, InvitationCode
from django.views.generic import TemplateView
from django.http import HttpResponse
import json

def Upload(request):
    for item in request.FILES:
        obj=request.FILES.get(item)
        filename=obj.name
        with open('FILES'+filename,'wb') as f:
            for line in obj.chunks():
                f.write(line)
    return  HttpResponse(json.dumps(['true']))

class Index(TemplateView):
    pass

def index(request,username):
    return render(request,'filebrowser/member_index.html')