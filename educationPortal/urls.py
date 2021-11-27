from os import stat
from django.conf.urls import url
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("createNewClassroom/<str:name>/", views.createNewClassroom,
         name="createNewClassroom"),
    path("ViewClassroom/<str:code>/", views.ViewClassroom, name="ViewClassroom"),
    path("JoinClassroom/<str:code>/",
         views.JoinClassroom, name="JoinClassroom"),
    path("makeAnnouncement/", views.makeAnnouncement, name="makeAnnouncement"),
    path("addComment/", views.addComment, name="addComment"),
    path("editProfileImage/", views.editProfileImage, name="editProfileImage"),  
]
