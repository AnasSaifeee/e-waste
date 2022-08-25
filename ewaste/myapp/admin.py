from django.contrib import admin
from myapp.models import Dform, Profile
from myapp.models import extendeduser
admin.site.register(extendeduser)
admin.site.register(Dform)
admin.site.register(Profile)
