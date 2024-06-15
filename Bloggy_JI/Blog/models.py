from django.db import models

# Create your models here.
from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User
from django.utils.html import format_html


# Create your models here.

class Category(models.Model):
    cat_id = models.AutoField(primary_key=True)
    title = models.CharField(unique=True, max_length=100)
    desc = models.TextField()
    image = models.ImageField(upload_to='category/', default="")
    date = models.DateField(default=now, null=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return format_html(
            '<img src="/media/{}" style="height:50px; width:50px; border-radius:50%;"/>'.format(self.image))


# Upload Blog
class Blog_Post(models.Model):
    b_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField(blank=True, default=now)
    likes = models.IntegerField(default=0, blank=True)
    views = models.IntegerField(blank=True, default=0)
    thumbnail = models.ImageField(upload_to='Thumbnail/', default="")

    def __str__(self):
        return str(self.title) + ' By ' + str(self.user)


class Upload_Video(models.Model):
    v_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(blank=True, default=now)
    likes = models.IntegerField(default=0, blank=True)
    views = models.IntegerField(blank=True, default=0)
    video_file = models.FileField(upload_to='video/', default="")

    def __str__(self):
        return str(self.title) + ' By ' + str(self.user)


class Upload_Image(models.Model):
    i_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(blank=True, default=now)
    likes = models.IntegerField(default=0, blank=True)
    views = models.IntegerField(blank=True, default=0)
    image_file = models.ImageField(upload_to='Images/', default="")

    def __str__(self):
        return str(self.title) + ' By ' + str(self.user)


class Blog_Comment(models.Model):
    c_no = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Blog_Post, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return "Comment By " + str(self.user)


class Video_Comment(models.Model):
    c_no = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Upload_Video, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return "Comment By " + str(self.user)


class Image_Comment(models.Model):
    c_no = models.AutoField(primary_key=True)
    comment = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Upload_Image, on_delete=models.CASCADE)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True)
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return "Comment By " + str(self.user)


class Content(models.Model):
    c_no = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    input = models.TextField()
    content = models.TextField()
    timestamp = models.DateTimeField(default=now)

    def __str__(self):
        return str(self.input)
