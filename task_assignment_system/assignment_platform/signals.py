from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.shortcuts import redirect
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created in kwargs:
        Profile.objects.create(user=instance)
    else:
        return redirect('login')

@receiver(post_save, sender=User)
def save_profile(sender, instance, created,**kwargs):
    if created in kwargs:
        instance.profile.save()
    else:
        return redirect('login')