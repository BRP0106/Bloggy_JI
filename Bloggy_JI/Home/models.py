from django.db import models


# Create your models here.
class Contact(models.Model):
    s_no = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=13)
    issue = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return 'Message From ' + str(self.name)
