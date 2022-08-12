from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

class UserManager(BaseUserManager):

    def create_user(self, email, firstname, lastname, password, **other_fields):

        email = self.normalize_email(email)
        user = self.model(email=email, firstname=firstname, lastname=lastname, **other_fields)

        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, email, firstname, lastname, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        return self.create_user(email, firstname, lastname, password, **other_fields)


class User(AbstractBaseUser, PermissionsMixin):

    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)

    email = models.EmailField(unique=True)

    username = models.CharField(max_length=50, unique=True)

    is_staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['firstname', 'lastname', 'username']

    objects = UserManager()

    def __str__(self):
        return self.username