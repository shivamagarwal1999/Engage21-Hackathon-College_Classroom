from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.fields import CharField
import os



class User(AbstractUser):
    userType = models.CharField(max_length=20, default="student")
    profile_pic = models.ImageField(
        upload_to='uploads/', blank=True, default="blankUserIcon.svg")


class Classroom(models.Model):
    name = models.CharField(max_length=100, default="Classroom")
    students = models.ManyToManyField(User, blank=True)
    teacher = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="teacher")
    code = models.CharField(max_length=20)
    subject = models.CharField(max_length=50, default="")
    theme = models.CharField(max_length=20, default="cardBlue")


class Comment(models.Model):
    date = models.DateTimeField(null=True)
    text = CharField(max_length=5000, default="")
    commenter = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter", null=True)


class Announcement(models.Model):
    classroom = models.ForeignKey(
        Classroom, on_delete=models.CASCADE, related_name="classroom", null=True)
    body = CharField(max_length=20000, default="")
    creator = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="creator", null=True)
    date = models.DateTimeField(null=True)
    comments = models.ManyToManyField(Comment, blank=True)





class FileModel(models.Model):
    file = models.FileField(blank=True,upload_to ='uploads/')
    def name(self):
        return os.path.basename(self.file.name)


