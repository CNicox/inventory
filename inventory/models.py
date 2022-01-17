from django.db import models
from datetime import datetime
# Create your models here.

'''
how to apply changes to the database (to models):
python manage.py makemigrations (commit changes)
python manage.py migrate (applies)
'''
#test commit


class Item(models.Model):
    name = models.CharField(max_length=128)
    item_model = models.CharField(max_length=128, blank=True)
    order_number = models.CharField(max_length=64, blank=True)
    model_number = models.CharField(max_length=64, blank=True)
    serial_number = models.CharField(max_length=128, blank=True)
    properties =  models.CharField(max_length=500, blank=True)
    assignment_date = models.DateTimeField(blank=True) # need to configure so that this field refreshes each time a person field is changed
    notes = models.CharField(max_length=1000, blank=True)
    #here are those additional fields
    pin = models.CharField(max_length=10, blank=True)
    puk = models.CharField(max_length=10, blank=True)
    mobile_number = models.CharField(max_length=24, blank=True)

    owner = models.ForeignKey("Person", on_delete=models.SET_NULL, blank=True, null=True, related_name="items")
    equipment_category = models.ForeignKey('Equipment_category', on_delete=models.SET_NULL, null=True,
                                           related_name="items")  # if Equipment_category is deleted the value is set to 0 and items is how the field is referenced from Equipment_category
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, related_name="items")
    def __str__(self):
        return f'{self.name}'


class Comment(models.Model):
    text = models.CharField(max_length=512)
    author = models.CharField(max_length=128)
    published = models.DateTimeField(default=datetime.now)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='comments')

#add str def
class Person(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    mobile_number = models.CharField(max_length=24, blank=True)
    email = models.EmailField(max_length=254, blank=True)
    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Equipment_category(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'

class Department(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.name}'








'''
as info for on_delete
CASCADE: When the referenced object is deleted, also delete the objects that have references to it (when you remove a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.
PROTECT: Forbid the deletion of the referenced object. To delete it you will have to delete all objects that reference it manually. SQL equivalent: RESTRICT.
RESTRICT: (introduced in Django 3.1) Similar behavior as PROTECT that matches SQL's RESTRICT more accurately. (See django documentation example)
SET_NULL: Set the reference to NULL (requires the field to be nullable). For instance, when you delete a User, you might want to keep the comments he posted on blog posts, but say it was posted by an anonymous (or deleted) user. SQL equivalent: SET NULL.
SET_DEFAULT: Set the default value. SQL equivalent: SET DEFAULT.
SET(...): Set a given value. This one is not part of the SQL standard and is entirely handled by Django.
DO_NOTHING: Probably a very bad idea since this would create integrity issues in your database (referencing an object that actually doesn't exist). SQL equivalent: NO ACTION.
'''