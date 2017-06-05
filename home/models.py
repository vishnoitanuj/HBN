from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Innovation(models.Model):
    innovator = models.CharField(max_length= 250, blank=True)
    title = models.CharField(max_length=250)
    brief = models.CharField (max_length=100)
    image = models.FileField(default='hbnlogo.png')
    detail = models.TextField(blank=True)
    file = models.FileField(blank=True)
    updatedtime = models.DateField(auto_now=True, auto_now_add=False)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)

    def get_absolute_url(self):
        return reverse('home:detail',kwargs={'pk': self.pk})

    def __str__(self):
        return self.innovator+' - '+self.title

    class Meta:
        ordering = ["-updatedtime","-timestamp"]


class Activities(models.Model):
    act_title=models.CharField(max_length=100)
    act_logo=models.FileField(blank=True)

    def __str__(self):
        return self.act_title+' - '+self.act_logo


class Announcement(models.Model):
    title = models.CharField(max_length=30)
    url = models.URLField(max_length=500)
    date = models.DateField(auto_now=False)
    type = models.CharField(max_length=10)
    head = models.BooleanField(default=False)

    def __str__(self):
        return self.title
