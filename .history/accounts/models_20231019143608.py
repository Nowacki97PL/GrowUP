from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser
from imagekit.models import ImageSpecField
from pilkit.processors import ResizeToFill
from django.db.models.signals import post_save
from django.dispatch import receiver


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email address")

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, type_of_user, password=None):
        jobs = [
            "Trener Personalny", "Trener Personalny",
            "Trener Mentalny", "Trener Mentalny",
            "Dietetyk"
        ]
        user = self.create_user(
            email,
            password=password,
            
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name="email address",
        max_length=255,
        unique=True,
    )
    entries = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = "email"

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class UserProfile(models.Model):
    avatar = models.ImageField(upload_to="media/avatars/", blank=True, null=True)
    avatar_thumbnail = ImageSpecField(
        source="avatar",
        processors=[ResizeToFill(360, 360)],
        format="JPEG",
        options={"quality": 80},
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    phone = models.CharField(max_length=32)
    user = models.OneToOneField(MyUser, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, null=True)
    last_name = models.CharField(max_length=30, null=True)
    address = models.CharField(max_length=256, null=True)
    post_code = models.CharField(max_length=32, null=True)
    city = models.CharField(max_length=64, null=True)
    country = models.CharField(max_length=64, null=True)
    

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    @receiver(post_save, sender=MyUser)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            UserProfile.objects.create(user=instance)
            