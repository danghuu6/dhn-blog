from django.contrib import admin
from .models import Posts, Categories, Comment
# Register your models here.


admin.site.register(Posts)
admin.site.register(Categories)
admin.site.register(Comment)

