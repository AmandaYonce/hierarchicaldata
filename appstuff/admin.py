from django.contrib import admin
from appstuff.models import File
from mptt.admin import DraggableMPTTAdmin

admin.site.register(File, DraggableMPTTAdmin)
