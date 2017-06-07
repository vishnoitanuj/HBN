
from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.urlresolvers import reverse


def upload_location(instance, filename):
    return "%s/%s"%(instance.id,filename)
# Create your models here.
class Innovation(models.Model):
    innovator = models.CharField(max_length= 250, blank=True)
    title = models.CharField(max_length=250)
    location = models.CharField(max_length=100)
    image = models.ImageField(
        upload_to=upload_location,
        width_field="width_field",
        height_field='height_field',
        default='hbnlogo.png')
    width_field=models.IntegerField(default=0)
    height_field=models.IntegerField(default=0)
    detail = models.TextField(blank=True)
    file = models.FileField(blank=True)
    updatedtime = models.DateField(auto_now=True, auto_now_add=False)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    tag = models.CharField(max_length=50, blank=True, default='guest')

    def get_absolute_url(self):
        return reverse('home:detail',kwargs={'pk': self.pk})

    def __str__(self):
        return self.innovator+' - '+self.title

    class Meta:
        ordering = ["-updatedtime","-timestamp"]


class Activities(models.Model):
    act_title=models.CharField(max_length=100)
    back = models.FileField()
    act_logo=models.FileField(blank=True,default='hbnlogo.png')
    act_url=models.CharField(max_length=50,blank=True)
    act_detail = models.TextField(blank=True)
    act_timestamp = models.DateField()

    def __str__(self):
        return self.act_title+' - '+self.act_url


class Announcement(models.Model):
    title = models.CharField(max_length=30)
    url = models.URLField(max_length=500)
    date = models.DateField(auto_now=False)
    type = models.CharField(max_length=10)
    head = models.BooleanField(default=False)

    def __str__(self):
        return self.title



class NetworkMember(models.Model):
    name = models.CharField(max_length=50)
    picture = models.FileField()

    def __str__(self):
        return self.name

class Suggestion(models.Model):
    message = models.TextField(blank=True)
    posted_on = models.DateTimeField(auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.posted_on