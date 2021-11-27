from datetime import date, datetime, time
import educationPortal
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.backends import AllowAllUsersModelBackend
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.http.response import JsonResponse
from django.shortcuts import render
from django.urls import reverse
import json
from .models import  *
from django.shortcuts import redirect
import uuid
import sys
from django.db.models import Q
import time
from django.core.mail import send_mail
from django.core import serializers
import boto3
import os


def index(request):
    if request.user.is_authenticated:

    

        if request.user.userType.lower() == "teacher":
            allClasses = Classroom.objects.all().filter(teacher=request.user)
            return render(request, "educationPortal/index.html", {
                "classes": allClasses,
                "user": request.user,
                
            })
        if request.user.userType.lower() == "student":
            allClasses = Classroom.objects.filter(students=request.user)
            print(allClasses)
            return render(request, "educationPortal/index.html", {
                "classes": allClasses,
                "user": request.user,
            
            })

    else:
        return login_view(request)


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "educationPortal/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "educationPortal/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]

        userType = request.POST["userType"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "educationPortal/register.html", {
                "message": "Passwords must match."
            })
        if email.split("@")[-1]!="nsec.ac.in":
            return render(request, "educationPortal/register.html", {
                "message": "Only @nsec.ac.in emails are allowed"
            })
        # Attempt to create new user
        try:
            if User.objects.filter(email=email).first():
                return render(request, "educationPortal/register.html", {
                "message": "Email already taken."})
            user = User.objects.create_user(username, email, password)
            user.first_name = firstname
            user.last_name = lastname
            user.userType = userType
            user.profile_pic = request.FILES.get('img')
            user.save()
        except IntegrityError:
            return render(request, "educationPortal/register.html", {
                "message": "Username already taken."
            })
        #login(request, user)
        return HttpResponseRedirect(reverse("login"))
    else:
        return render(request, "educationPortal/register.html")


def createNewClassroom(request, name):
    if request.method == "POST":
        data = json.loads(request.body)
        name = data["name"]

        classroom = Classroom()
        classroom.name = name
        classroom.teacher = request.user
        classroom.theme = data["theme"]
        classroom.subject = data["subject"]

        allclasses = Classroom.objects.all()
        code = uuid.uuid4().hex[:8].upper()
        unique = True
        for c in allclasses:
            if c.code == code:
                unique = False

        # checking for uniqueness of code
        while unique == False:
            code = uuid.uuid4().hex[:8].upper()
            for c in allclasses:
                if c.code == code:
                    unique = False

        classroom.code = code
        classroom.save()

    elif request.method == "DELETE":
        data = json.loads(request.body)
        id = data["id"]
        allclasses = Classroom.objects.filter(id=id).delete()

    return HttpResponse()


def JoinClassroom(request, code):
    if request.method == "GET":

        set = Classroom.objects.all().values_list('code', flat=True)
        codes = []
        for s in set:
            codes.append(s)

        return JsonResponse({
            'codes': codes
        })

    if request.method == "PUT":
        data = json.loads(request.body)
        code = data["code"]

        classroom = Classroom.objects.get(code=code)
        classroom.students.add(request.user)
        classroom.save()
        print('hey')
        return render(request, "educationPortal/ViewClassroom.html", {
            "class": classroom
        })

    if request.method == "DELETE":
        data = json.loads(request.body)
        code = data["code"]

        classroom = Classroom.objects.get(code=code)
        classroom.students.remove(request.user)
        classroom.save()

        return render(request, "educationPortal/ViewClassroom.html", {
            "class": classroom
        })


def ViewClassroom(request, code):
    if request.user.is_authenticated:
        selectedClass = Classroom.objects.get(code=code)

        announcements = Announcement.objects.filter(
            classroom=selectedClass).order_by('-date')

        return render(request, "educationPortal/ViewClassroom.html", {
            "class": selectedClass,
            "announcements": announcements
        })
    else:
        return login_view(request)


def makeAnnouncement(request):

    if request.method == "POST":
        data = json.loads(request.body)
        print()

        announcement = Announcement()
        announcement.body = data["body"]
        announcement.creator = request.user
        announcement.date = datetime.now()
        announcement.classroom = Classroom.objects.get(code=data["code"])

        announcement.save()

    return HttpResponse()


def addComment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print(data["text"])
        print(data["id"])

        comment = Comment()
        comment.commenter = request.user
        comment.text = data["text"]
        comment.date = datetime.now()
        comment.save()

        announcement = Announcement.objects.get(id=data["id"])
        announcement.comments.add(comment)
        announcement.save()

    return HttpResponse()

def editProfileImage(request):
    if request.method == "POST":
        user = request.user
        # print(request.__dict__, file=sys.stderr)
        user.profile_pic.delete()
        user.profile_pic = request.FILES.get('img')
        user.save()
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


