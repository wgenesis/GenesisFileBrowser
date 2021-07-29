from django.db import models
from user.models import Member
# Create your models here.

class Folder(models.Model):
    folder_name=models.CharField(max_length=128)
    members=models.ManyToManyField(
        Member,
        through=('FolderShip'),
        through_fields=('folder','member'),
    )

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
    folder=models.ForeignKey(Folder,on_delete=models.CASCADE)
    file=models.ForeignKey(File,on_delete=models.CASCADE)

class FolderShip(models.Model):
    member=models.ForeignKey(Member,on_delete=models.CASCADE)
    folder=models.ForeignKey(Folder,on_delete=models.CASCADE)
    upload_time=models.DateTimeField(auto_now_add=True)


