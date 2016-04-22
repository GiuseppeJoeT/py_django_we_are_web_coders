from django.db import models
from django.conf import settings
from django.utils import timezone
from signals import subscription_was_cancelled, subscription_created
from paypal.standard.ipn.signals import subscription_signup, subscription_cancel


class Magazine(models.Model):

    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    subscription_signup.connect(subscription_created)
    subscription_cancel.connect(subscription_was_cancelled)

    def __unicode__(self):
        return self.name


class Purchase(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='purchases')
    magazine = models.ForeignKey(Magazine)
    subscription_end = models.DateTimeField(default=timezone.now)
