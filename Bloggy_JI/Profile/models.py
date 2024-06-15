from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Profile(models.Model):
    p_id = models.AutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='Profile_Photo/', default=True, null=True)
    bio = models.CharField(max_length=200)

    def __str__(self):
        return self.user.username
