from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

import base64
import os
# Create your models here.

class Candidate(models.Model):
    sno = models.IntegerField(unique=True)
    name = models.CharField(blank=False, max_length=50)
    email = models.EmailField(blank=False)
    mobile = models.CharField(blank=False, null=True, max_length=50)
    work_exp = models.FloatField(default=0.0)
    resume = models.CharField(blank=True, null=True, max_length=5)
    current_loc = models.CharField(blank=True, null=True, max_length=50)
    nearest_loc = models.CharField(blank=True, null=True, max_length=50)
    ctc = models.FloatField(default=0.0)
    current_employer = models.CharField(blank=True, null=True, max_length=50)
    current_desig = models.CharField(blank=True, null=True, max_length=50)
    ug_course = models.CharField(blank=True, null=True, max_length=50)
    ug_institute = models.CharField(blank=True, null=True, max_length=50)
    trier_1 = models.CharField(blank=True, null=True, max_length=50)
    ug_pass_year = models.CharField(blank=True, null=True, max_length=50)
    pg_course = models.CharField(blank=True, null=True, max_length=50)
    pg_institute = models.CharField(blank=True, null=True, max_length=50)
    pg_pass_year = models.CharField(blank=True, null=True, max_length=50)
    preferred_loc = models.CharField(max_length=200)
    skills = models.TextField(null=True, blank=True)

    def __str__(self):
        return str(self.name)