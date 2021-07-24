from django.shortcuts import render
from django.shortcuts import redirect
from user.models import Member, InvitationCode
import json

# Create your views here.

def Index(request):
    return render(request, 'login/index.html')

def Login(request):
    if request.method == 'POST':
        form_data = request.POST.copy()
        if 'username' in form_data:
            username = form_data.get('username')
            password = form_data.get('password')
            try:
                user_obj = Member.objects.get(username=username)
            except:
                return render(request, 'login/login.html')
            if user_obj.password == password:
                return redirect('/index/')
        elif 'usernameRegister' in form_data:
            if not Member.objects.filter(username=form_data['usernameRegister']):
                if not Member.objects.filter(student_id=form_data['studentID']):
                    if InvitationCode.objects.filter(code=form_data['invitationCode']):
                        invitation_code=InvitationCode.objects.get(code=form_data['invitationCode'])
                        Member.objects.create(real_name=form_data['realName'],
                                              username=form_data['usernameRegister'],
                                              student_id=form_data['studentID'],
                                              password=form_data['registerPassword'],
                                              permission=invitation_code.permission,
                                              )
                        return redirect('/index/')
                    else:
                        return render(request, 'login/login.html', {
                            'result': json.dumps({'fail':'invitation'})
                        })
                else:
                    return render(request, 'login/login.html', {
                        'result': json.dumps({'fail': 'studentId'})
                    })
            else:
                return render(request, 'login/login.html', {
                    'result': json.dumps({'fail': 'usernameRegister'})
                })
    return render(request, 'login/login.html')


def RegisterVaild(request):
    if request.method == 'POST':
        return render(request, 'login/register.html')


def Logout(request):
    return redirect('/login/')
