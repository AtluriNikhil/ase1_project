# Generated by Django 3.0.8 on 2020-07-20 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userinfo', '0013_auto_20200720_1132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, default='profile_pics/default.jpg', upload_to='profile_pics'),
        ),
    ]
