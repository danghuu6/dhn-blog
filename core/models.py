from django.db import models
from tinymce import models as tinymce_models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
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


class UserManager(BaseUserManager):
    def create_user(self, user_name, full_name, password=None):
        if not user_name:
            raise ValueError('user name is required')
        if not full_name:
            raise ValueError('full name is required')

        user = self.model(
            user_name=user_name,
            full_name=full_name,
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, user_name, full_name, password=None):
        user = self.create_user(
            user_name=user_name,
            full_name=full_name,
            password=password
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)

        return user


class User(AbstractBaseUser):
    user_name = models.CharField(max_length=255, primary_key=True)
    full_name = models.CharField(max_length=255, default='')
    time = models.DateTimeField(auto_now=True)
    last_login = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'user_name'
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    def __str__(self):
        return self.full_name

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True
