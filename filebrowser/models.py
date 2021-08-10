from django.db import models
from django.utils import timezone
from user.models import Member
# Create your models here.

class Organization(models.Model):
    Organization_name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.Organization_name

class Folder(models.Model):
    folder_name=models.CharField(max_length=128)
    organization=models.ForeignKey(Organization,on_delete=models.CASCADE,null=True)
    parent_folder=models.ForeignKey('self',on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.folder_name

class File(models.Model):
    folders = models.ManyToManyField(
        Folder,
        through='Fileship',
        through_fields=('file','folder'),
    )
    file_name=models.CharField(max_length=128)
    storage_file_name=models.CharField(max_length=128,unique=True)
    MD5=models.CharField(max_length=128,unique=True)
    file_size=models.IntegerField()
    file_type=models.CharField(max_length=10)

    def __str__(self):
        return self.file_name

class Fileship(models.Model):
    file=models.ForeignKey(File,on_delete=models.CASCADE)
    folder=models.ForeignKey(Folder,on_delete=models.CASCADE)
    upload_time = models.DateTimeField(auto_now_add=True)

# class OrganizationShip(models.Model):
#     folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
#     organization=models.ForeignKey(Organization,on_delete=models.CASCADE)




