from django.contrib.auth.models import User
from django.db import models


class history(models.Model):
    name_of_student = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    name_of_book = models.CharField(max_length=111, blank=True, null=True)
    code_no = models.CharField(max_length=222, blank=True, null=True)
    code_of_book = models.IntegerField(blank=True, null=True)
    issued_date = models.DateField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    returned_date = models.DateField(null=True, blank=True)