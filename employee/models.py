from django.db import models
from django.db.models.signals import pre_save

from .utils import unique_slug_generator

class Employee(models.Model):
    firstName   = models.CharField(max_length=220)
    lastName	= models.CharField(max_length=220)
    slug        = models.SlugField(unique=True, blank=True)
    email       = models.CharField(max_length=120, help_text='Ingrese Correo Electronico', null=True, blank=True)
    featured    = models.BooleanField(default=False)
    mobileNumber = models.IntegerField()
    createdAt   = models.DateTimeField(auto_now_add=True)
    updatedAt   = models.DateTimeField(auto_now_add=True)

    def __str__(self): # __unicode__
        return self.firstName

    @property
    def title(self):
        return self.firstName


def employee_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(employee_pre_save_receiver, sender=Employee)