from django.contrib import admin
# from basic_app.models import UserProfileInfo
from hyper.apps.models import Project, Tag

# Register your models here.
admin.site.register(Project)
admin.site.register(Tag)
