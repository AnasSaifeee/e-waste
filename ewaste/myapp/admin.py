from django.contrib import admin
from myapp.models import Dform, Profile
from myapp.models import Contributor,Collector
admin.site.register(Contributor)
admin.site.register(Collector)
admin.site.register(Dform)
admin.site.register(Profile)
