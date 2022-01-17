from django.contrib import admin
from .models import *

"""
how to create admin console
python manage.py createsuperuser admin admin500!
runserver and they should be there
"""

admin.site.register(Item)
admin.site.register(Comment)
admin.site.register(Person)
admin.site.register(EquipmentCategory)
admin.site.register(Department)
admin.site.register(MobilePhone)




# Register your models here.
