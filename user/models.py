from django.db import models
import datetime
# Create your models here.

class Person(models.Model):
    real_name=models.CharField(max_length=20,default='real_name')
    student_id=models.IntegerField(unique=True)
    
    class Meta:
        #定义为抽象基类
        abstract=True

class Group(models.Model):
    #小组模型
    work=models.CharField(max_length=20)

class Member(Person):
    #成员模型
    groups = models.ManyToManyField(
        Group,
        through='Membership',
        through_fields=('member','group'),
    )
    username=models.CharField(max_length=15,default='username')
    permission=models.IntegerField()
    password = models.CharField(max_length=256,default='password')
    sign_up_time=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.real_name

    class Meta:
        ordering = ["-sign_up_time"]
        verbose_name = "用户"
        verbose_name_plural = "用户"

class Membership(models.Model):
    #成员关系中间表
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    inviter = models.CharField(max_length=20)

class InvitationCode(models.Model):
    #邀请码
    code=models.CharField(max_length=10)
    generate_date=models.DateTimeField(auto_now_add=True)
    permission = models.IntegerField()
    owner=models.ForeignKey(Member,on_delete=models.CASCADE)

