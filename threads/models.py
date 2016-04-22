from django.db import models
from django.utils import timezone
from tinymce.models import HTMLField
from django.conf import settings


class Subject(models.Model):
    name = models.CharField(max_length=255)
    description = HTMLField(default='')

    #  description --> is a field that comes packaged with django-tinymce
    # it enables our field to render the WYSIWYG editor in our admin

    def __unicode__(self):
        return self.name


class Thread(models.Model):
    name = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='threads')
    subject = models.ForeignKey(Subject, related_name='threads')
    created_at = models.DateTimeField(default=timezone.now)


class Post(models.Model):
    thread = models.ForeignKey(Thread, related_name='posts')
    comment = HTMLField(blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='posts')
    created_at = models.DateTimeField(default=timezone.now)

'''
We are using the ForeignKey field to connect out many posts to one
single thread, and to link back to the user who created the post.
'''
