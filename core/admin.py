from django.contrib import admin
from .models import Posts, Categories, Comment, User
from django.contrib.auth.hashers import make_password
# Register your models here.


class BlogAdmin(admin.AdminSite):
    site_header = 'DHN Blog'


admin_site = BlogAdmin(name='blog_admin')

# admin_site.unregister(Group)
admin_site.register(Posts)
admin_site.register(Categories)


class PermUserAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        obj.password = make_password(obj.password)
        obj.user = request.user
        obj.save()

    def has_add_permission(self, request):
        if request.user.is_admin:
            return True
        return False

    def has_change_permission(self, request, obj=None):
        if request.user.is_admin:
            return True
        return False

    def has_delete_permission(self, request, obj=None):
        if request.user.is_admin:
            return True
        return False

    def has_view_permission(self, request, obj=None):
        if request.user.is_admin or request.user.is_staff:
            return True
        return False


admin_site.register(Comment, PermUserAdmin)
admin_site.register(User, PermUserAdmin)
