from django.shortcuts import render
from django.shortcuts import redirect
from user.models import Member, InvitationCode
from django.http import HttpResponse
import json

def Upload(request):
    print("前端数据：",request.POST)
    print("file",request.FILES)
    for item in request.FILES:
        obj=request.FILES.get(item)
        filename=obj.name
        with open(filename,'wb') as f:
            for line in obj.chunks():
                f.write(line)
    return HttpResponse(json.dumps(['true']))

def member_index(request):
    return render(request,'filebrowser/member_index.html')