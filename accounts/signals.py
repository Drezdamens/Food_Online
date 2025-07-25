from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile

@receiver(post_save, sender=User) # the same as the 103 row
def post_save_create_profile_receiver(sender, instance, created,**kwargs):
    print(created)
    if created:
        UserProfile.objects.create(user=instance)
        print('user profile created')
    else:
        try:

            profile = UserProfile.objects.get(user=instance)
            profile.save()
        except:
            # Create the userprofile if not exist
            UserProfile.objects.create(user=instance)
            print('profile was not exist, but i created one')
        print('user profile updated')


@receiver(pre_save, sender=User)
def pre_save_profile_receiver(sender, instance, **kwargs):
    pass
#post_save.connect(post_save_create_profile_receiver, sender=User)
