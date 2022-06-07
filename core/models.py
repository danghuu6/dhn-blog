from django.db import models
from tinymce import models as tinymce_models
# Create your models here.


class Categories(models.Model):
    categories_id = models.CharField(max_length=10, primary_key=True)
    categories_name = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.categories_name


class Posts(models.Model):
    categories = models.ForeignKey(Categories, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=255, default='')
    content = tinymce_models.HTMLField()
    time = models.DateTimeField(auto_now=True)
    public = models.BooleanField(default=False)
    image = models.TextField(default='')

    def __str__(self):
        return self.title


class Comment(models.Model):
    posts_id = models.ForeignKey(Posts, on_delete=models.DO_NOTHING)
    comment_user = models.CharField(max_length=255, default='')
    comment_email = models.CharField(max_length=255, default='', null=True)
    comment_content = models.TextField(default='')
    time = models.DateTimeField(auto_now=True)

