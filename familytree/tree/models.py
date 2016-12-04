from __future__ import unicode_literals
from django.contrib.auth.base_user import AbstractBaseUser

from django.db import models

class FTUser(AbstractBaseUser):
	pass

class Tree(models.Model):
	creator = models.ForeignKey(FTUser)
	name = models.CharField(max_length=200)
