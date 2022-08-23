from django.contrib import admin
from myapp.models import Dform
from myapp.models import extendeduser
admin.site.register(extendeduser)
admin.site.register(Dform)
