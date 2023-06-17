from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin ,AbstractUser
from app.managers import MyUserManager
from django.conf import settings

# Create your models here.



class MyUser(AbstractBaseUser,PermissionsMixin):

    email = models.EmailField(verbose_name='email address',max_length=255,blank=True,unique=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(("staff status"),
        default=False,
        help_text=(
            "Designates that this user can log into the admin site "

        ))

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [] #required while creating a superuser

    def __str__(self):
        return self.email
    
class MusicFile(models.Model):
    MUSIC_VISIBILITY_CHOICES = (
        ('Public', 'Public'),
        ('Private', 'Private'),
        ('Protected', 'Protected'),
    )

    title = models.CharField(max_length=100)
    file = models.FileField(upload_to='music')
    image = models.ImageField(upload_to='song_images',null=True)
    singer = models.CharField(max_length=250,null=True)
    visibility = models.CharField(max_length=10, choices=MUSIC_VISIBILITY_CHOICES, default='Public')
    emails = models.ManyToManyField(MyUser,blank=True , related_name='protected_music')
    uploader = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    
    def all_emails(self):
        return ",".join([str(p) for p in self.emails.all()])





