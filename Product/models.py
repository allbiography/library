from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


# to attach more info in user model

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    grade = models.CharField(max_length=22)


class personal_info(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True)
    profile_picture = models.ImageField(upload_to='images/', blank=True, null=True)
    faculty = models.CharField(max_length=222, blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    section = models.CharField(max_length=222, blank=True, null=True)
    first_ordered_book = models.CharField(max_length=20, blank=True, null=True)
    second_ordered_book = models.CharField(max_length=20, blank=True, null=True)


def __str__(self):
    return self.user.username


class Meta:
    db_table = "personal_info"


@receiver(post_save, sender=User)
def create_or_update_user_profile(sender, instance, created, **kwargs):
    if created:
        personal_info.objects.create(user=instance)
    instance.personal_info.save()


# def __str__(self):
#     return f'{self.student_nam


#
# to link the personal_info with Book_Order
# @property
# def name(self):
#     return self.name_of_student.name


class Text_Book(models.Model):
    name = models.CharField(max_length=222, blank=True, null=True)
    code_no = models.CharField(max_length=222, blank=True, null=True)
    writer = models.CharField(max_length=22, null=True)
    description = models.TextField(max_length=2222, blank=True, null=True)
    price = models.FloatField(null=True, blank=True)
    stock = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(max_length=8888, blank=True, null=True)
    book_pic = models.ImageField(upload_to='books/', null=True, blank=True)


class Programming_Book(models.Model):
    name = models.CharField(max_length=222, blank=True, null=True)
    code_no = models.CharField(max_length=222, blank=True, null=True)
    writer = models.CharField(max_length=22, null=True, blank=True)
    description = models.TextField(max_length=2222, blank=True, null=True)
    price = models.FloatField(null=True, blank=True)
    stock = models.IntegerField(blank=True, null=True)
    image_url = models.CharField(max_length=8888, blank=True, null=True)
    student = models.CharField(max_length=299, null=True, blank=True)
    teacher = models.CharField(max_length=100, blank=True)

    class Meta:
        db_table = "product_programming_book"
