from typing import Text
from django.contrib import admin

from .models import *

admin.site.register(User)
admin.site.register(Classroom)

admin.site.register(FileModel)

admin.site.register(Comment)
