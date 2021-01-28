import random
import string
from django.db import models


def code_generator(size=6, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def create_shortcode(instance, size=6):
    new_code = code_generator(size=size)
    klass=instance.__class__
    qs_exists=klass.objects.filter(shortcode=new_code).exists()
    if qs_exists:
        return create_shortcode(size=size)
    return new_code


class Urlshort(models.Model):
    url = models.CharField(max_length=200)
    shortcode = models.CharField(max_length=15, unique=True, blank=True) # null=False, blank=False
    updated = models.DateTimeField(auto_now=True)
    count = models.IntegerField(default=1)
    timecreated = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if self.shortcode is None or self.shortcode == "":
            self.shortcode = create_shortcode(self)
        super(Urlshort, self).save(*args, **kwargs)

    def __str__(self):
        return str(self.url)
    
    def __unicode__(self):
        return self.url

