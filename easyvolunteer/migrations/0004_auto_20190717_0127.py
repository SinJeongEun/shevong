# Generated by Django 2.1.5 on 2019-07-17 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('easyvolunteer', '0003_auto_20190717_0115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cuser',
            name='another',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='cuser',
            name='area',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_area', to='easyvolunteer.Area'),
        ),
        migrations.AlterField(
            model_name='cuser',
            name='codeNum',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='cuser',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='cuser',
            name='job',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_job', to='easyvolunteer.Job'),
        ),
        migrations.AlterField(
            model_name='cuser',
            name='license',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='cuser',
            name='organ',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_organ', to='easyvolunteer.Organ'),
        ),
        migrations.AlterField(
            model_name='cuser',
            name='phoneNum',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
