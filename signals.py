from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import user_Profile


@receiver(post_save,sender=User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        user_Profile(user=instance)

@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    try:
        instance.user_profile.save()
    except :
        user_Profile(user=instance)

