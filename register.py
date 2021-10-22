from django.contrib import admin
from repository import models


from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from repository.models import UserProfile

from Forms.userprofile import UserCreationForm,UserChangeForm

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['username', 'gender', 'age', 'email', 'phone', 'jobs']
    list_filter = ['username', 'email', 'phone', 'jobs']
    search_fields = ['username', 'phone']
    filter_horizontal = ("agent", "upload_user",)

class RoleAdmin(admin.ModelAdmin):
    # list_display = ['name', 'menus', 'permissions',]

    filter_horizontal = ("permissions",)

# admin.site.register(models.Role, RoleAdmin)
admin.site.register(models.WorkPlace)
admin.site.register(models.Company)
admin.site.register(models.ResumeInfo)
admin.site.register(models.EducationInfo)
admin.site.register(models.Department)
admin.site.register(models.Project)
admin.site.register(models.PositionInfo)
admin.site.register(models.ProjectInfo)
admin.site.register(models.PersonalAssessment)
admin.site.register(models.WorkInfo)
admin.site.register(models.Keyword)
admin.site.register(models.ResumeWorkFlow)
admin.site.register(models.ResumeStatus)
admin.site.register(models.ResumeSourceText)
admin.site.register(models.ResumeSource)
admin.site.register(models.ResumeName)
admin.site.register(models.CustomLabel)
admin.site.register(models.Menu)
admin.site.register(models.SystemPermission)
admin.site.register(models.ComprehensiveAbility)
admin.site.register(models.Email)
admin.site.register(models.ResumeTemplate)
admin.site.register(models.SystemSetting)
admin.site.register(models.PreferreResumeTemplate)
admin.site.register(models.PreferreEmail)
admin.site.register(models.StatisticalDownloadResume)
admin.site.register(models.StoredEventType)
admin.site.register(models.EventLog)
admin.site.register(models.ResumeSubscription)
admin.site.register(models.Notification)
admin.site.register(models.Comment)

# admin.site.register(models.Group)


class UserProfileAdmin(BaseUserAdmin):
    # The forms to add and change user instances
    form = UserChangeForm
    add_form = UserCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('email', 'name', 'is_superuser',)
    list_filter = ('is_superuser',)
    fieldsets = (
        (None, {'fields': ('email', 'password', 'uuid')}),
        ('Personal info', {'fields': ('name', 'head_portrait', 'phone')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'user_permissions', 'groups')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ('user_permissions', 'groups')

# Now register the new UserAdmin...
admin.site.register(UserProfile, UserProfileAdmin)
# ... and, since we're not using Django's built-in permissions,
# unregister the Group model from admin.

# admin.site.unregister(Group)
