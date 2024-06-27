from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    # CustomUserManager methods not inherited
    def create_superuser(self, email, username, password, **other_fields):

        # setdefault gotten from django backend session
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError("Superuser must be assigned to is_staff=True")

        if other_fields.get('is_superuser') is not True:
            raise ValueError("Superuser must be assigned to is_superuser=True")

        return self.create_user(email, username, password, **other_fields)




        # making use of the create_user method in this place 


    # CustomUserManager methods not inherited
    def create_user(self, email, username, password, **other_fields):
        if not email:
            raise ValueError("You must provide an email address")

        # Using the methods from the inherited class (BaseUserManager): normalize_email, set_password
        email = self.normalize_email(email)
        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True)
    # password has been defined at the AbstractBaseUser class
    username = models.CharField(max_length=50)
    full_name = models.CharField(_('Full Name'),max_length=50)
    date_joined = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    #  



    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']


    def __str__(self):
        return self.username
        

