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
