from django.contrib import admin
from app.models import MyUser,MusicFile
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class MyUserAdmin(UserAdmin):
  
    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id','email')
    list_display_links = ('email',)
    list_filter = ('is_admin',)
    fieldsets = (
        ('user credential', {'fields': ('email','password',)}),
        ('Permissions', {'fields': ('is_admin','is_active','is_staff','is_superuser','groups','user_permissions')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email','id')

# Now register the new UserAdmin...
admin.site.register(MyUser,MyUserAdmin)

@admin.register(MusicFile)
class MusicFilesAdmin(admin.ModelAdmin):
    list_display = ['id','title','visibility','uploader','all_emails']
    list_display_links=['title']
