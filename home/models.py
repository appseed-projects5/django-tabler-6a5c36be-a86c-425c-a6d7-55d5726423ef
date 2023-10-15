# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Sysuser(models.Model):

    #__Sysuser_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    designation = models.CharField(max_length=255, null=True, blank=True)

    #__Sysuser_FIELDS__END

    class Meta:
        verbose_name        = _("Sysuser")
        verbose_name_plural = _("Sysuser")


class Resident(models.Model):

    #__Resident_FIELDS__
    fname = models.CharField(max_length=255, null=True, blank=True)
    mname = models.CharField(max_length=255, null=True, blank=True)
    lname = models.CharField(max_length=255, null=True, blank=True)
    alias = models.CharField(max_length=255, null=True, blank=True)
    birthplace = models.CharField(max_length=255, null=True, blank=True)
    bday = models.CharField(max_length=255, null=True, blank=True)
    civilstatus = models.CharField(max_length=255, null=True, blank=True)
    gender = models.CharField(max_length=255, null=True, blank=True)
    street = models.CharField(max_length=255, null=True, blank=True)
    houseno = models.CharField(max_length=255, null=True, blank=True)
    relationshiptoowner = models.CharField(max_length=255, null=True, blank=True)
    datecreated = models.CharField(max_length=255, null=True, blank=True)

    #__Resident_FIELDS__END

    class Meta:
        verbose_name        = _("Resident")
        verbose_name_plural = _("Resident")



#__MODELS__END
