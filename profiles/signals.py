from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import UserProfile


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    """
    Create a user profile for new users or update existing ones
    """
    if created:
        UserProfile.objects.create(user=instance)
    else:
        instance.userprofile.save()
