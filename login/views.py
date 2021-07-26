from django.shortcuts import render
from django.shortcuts import redirect
from user.models import Member, InvitationCode
from django.http import HttpResponse
import json

# Create your views here.

def Index(request):
    return render(request, 'login/index.html')

def Login(request):
    if request.method == 'POST':
        form_data = request.POST.copy()
        username = form_data.get('username')
        password = form_data.get('password')
        try:
            user_obj = Member.objects.get(username=username)
        except:
            return render(request, 'login/login.html')
        if user_obj.password == password:
            return redirect('/index/')
    return render(request, 'login/login.html')

def Register(request):
    if request.method == 'POST':
        form_data = request.POST.copy()
        invitation_code = InvitationCode.objects.get(code=form_data['invitationCode'])
        Member.objects.create(real_name=form_data['realName'],
                              username=form_data['usernameRegister'],
                              student_id=form_data['studentID'],
                              password=form_data['registerPassword'],
                              permission=invitation_code.permission,
                              )
        return redirect('/index/')
    return render(request, 'login/login.html')

def RegisterVaild(request):
    if request.method=='GET':
        vaild_type=request.GET.get('vaildType')
        vaild_value=request.GET.get('vaildValue')
        if vaild_type=='usernameRegister' and Member.objects.filter(username=vaild_value):
            return HttpResponse(json.dumps(['false']))

        if vaild_type=='studentID' and Member.objects.filter(student_id=int(vaild_value)):
            return HttpResponse(json.dumps(['false']))

        if vaild_type=='invitationCode' and not InvitationCode.objects.filter(code=vaild_value):
            return HttpResponse(json.dumps(['false']))

        return HttpResponse(json.dumps(['true']))


# def RegisterVaild(request):
#     if request.method == 'POST':
#         return render(request, 'login/register.html')


def Logout(request):
    return redirect('/login/')
