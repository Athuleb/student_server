# Generated by Django 4.2.16 on 2024-10-01 04:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_studentdetails_score_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentdetails',
            name='Score',
            field=models.IntegerField(default=0),
        ),
    ]
