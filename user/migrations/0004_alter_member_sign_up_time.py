# Generated by Django 3.2.5 on 2021-07-20 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210720_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='sign_up_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]