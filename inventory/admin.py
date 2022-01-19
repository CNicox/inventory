from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
"""
how to create admin console
python manage.py createsuperuser admin admin500!
runserver and they should be there
"""


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'is_admin')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),

        ('Permissions', {'fields': ('is_admin',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, UserAdmin)
admin.site.unregister(Group)

admin.site.register(Item)
admin.site.register(Comment)
admin.site.register(Person)
admin.site.register(EquipmentCategory)
admin.site.register(Department)
admin.site.register(MobilePhone)




# Register your models here.
