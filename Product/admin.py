from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from django.contrib.auth.admin import UserAdmin as BaseAdmin
from .models import *
from History_of_book.models import *


# add exel data to User models
class UserResource(resources.ModelResource):
    class Meta:
        # fields = (
        #     'username', 'id', 'password', 'last_login', 'is_superuser', 'groups', 'user_permissions', 'username',
        #     'first_name', 'last_name',
        #     'email', 'is_staff', 'is_active', 'date_joined', 'personal_info.grade',)
        model = User


class UserAdmin(BaseAdmin, ImportExportModelAdmin):
    resource_class = UserResource


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


# to edit user models
class personal_infoInline(admin.StackedInline):
    model = personal_info
    can_delete = False
    verbose_name_plural = 'personal_info'
    fk_name = 'user'


class CustomUserAdmin(UserAdmin):
    inlines = (personal_infoInline,)

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)


# import export for more personal_info
@admin.register(personal_info)
class personal_infoAdmin(ImportExportModelAdmin):
    list_display = ('user',)
    pass


# to add excel data in line 2 also
@admin.register(Programming_Book)
class Programming_BookAdmin(ImportExportModelAdmin):
    list_display = ('name', 'stock', 'code_no',)
    pass


# @admin.register(personal_info)
# class personal_infoAdmin(admin.ModelAdmin):
#     list_display = (
#         'student_name', 'profile_picture', 'first_ordered_book',
#         'second_ordered_book',)
#     ordering = ('student_name',)
#     search_fields = ('profile_picture',)


@admin.register(history)
class historyAdmin(ImportExportModelAdmin):
    list_display = ('name_of_student', 'name_of_book', 'code_of_book', 'issued_date', 'due_date', 'returned_date',)
    ordering = ('name_of_student',)
    search_fields = ('name_of_book', 'code_of_book',)
    pass


@admin.register(Text_Book)
class Text_BookAdmin(ImportExportModelAdmin):
    list_display = ('name', 'stock', 'book_pic',)
    ordering = ('name',)
    search_fields = ('name', 'writer', 'price', 'stock',)
    pass
