from django.contrib import admin
from myapp.models import Donor_form
from myapp.models import extendeduser
admin.site.register(extendeduser)
admin.site.register(Donor_form)