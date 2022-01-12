from django.contrib import admin
from .models import *

"""
how to create admin console
python manage.py createsuperuser admin admin500!
"""

admin.site.register(Item)
admin.site.register(Comment)
admin.site.register(Person)
admin.site.register(Equipment_category)
admin.site.register(Department)




# Register your models here.
