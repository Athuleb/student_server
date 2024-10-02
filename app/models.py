from django.db import models

# Create your models here.
class studentDetails(models.Model):
    stdId = models.IntegerField(primary_key=True)
    FirstName = models.CharField(max_length=100)
    LastName = models.CharField(max_length=100)
    Register = models.IntegerField(default=0)
    Email = models.EmailField(max_length=100)
    Course = models.CharField(max_length=100)
    Score = models.IntegerField(default=0)
    ProfileImage = models.ImageField(upload_to='student_images/', null=True, blank=True)