from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_email
from django.utils import timezone
import uuid

class UserManager(BaseUserManager):
    
    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError("You must provide a valid email address")
    
    def create_user(self, username, first_name, last_name, email, password, **extra_fields):
        if not username:
            raise ValueError("Users must have a username")

        if not first_name:
            raise ValueError("Users must have first name")

        if not last_name:
            raise ValueError("Users must have last name")


        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError("User email required")
    
        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )

        user.set_password(password)
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, first_name, last_name, email, password, **extra_fields):
        
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True")
        if not password:
            raise ValueError("Superuser must have password")
        
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError("Admin email required")
        
        user = self.create_user(username, first_name, last_name, email, password, **extra_fields)
        user.save(using=self._db)
        return user



class User(AbstractBaseUser, PermissionsMixin):

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    objects = UserManager()

    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    username = models.CharField(verbose_name=_("Username"), max_length=255, unique=True)
    first_name = models.CharField(verbose_name=_("First Name"), max_length=50)
    last_name = models.CharField(verbose_name=_("Last Name"), max_length=50)
    email = models.EmailField(verbose_name=_("Email Address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    


    def __str__(self):
        return self.username

    @property
    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def get_short_name(self):
        return self.username
