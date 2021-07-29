# Generated by Django 3.2.5 on 2021-07-29 21:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0007_auto_20210724_1748'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=128)),
                ('storage_file_name', models.CharField(max_length=128, unique=True)),
                ('MD5', models.CharField(max_length=128, unique=True)),
                ('file_size', models.IntegerField()),
                ('file_type', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder_name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='FolderShip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_time', models.DateTimeField(auto_now_add=True)),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filebrowser.folder')),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.member')),
            ],
        ),
        migrations.AddField(
            model_name='folder',
            name='members',
            field=models.ManyToManyField(through='filebrowser.FolderShip', to='user.Member'),
        ),
        migrations.CreateModel(
            name='Fileship',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filebrowser.file')),
                ('folder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='filebrowser.folder')),
            ],
        ),
        migrations.AddField(
            model_name='file',
            name='folders',
            field=models.ManyToManyField(through='filebrowser.Fileship', to='filebrowser.Folder'),
        ),
    ]