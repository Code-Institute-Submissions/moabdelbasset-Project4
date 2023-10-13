from django.db import models
from djrichtextfield.models import RichTextField
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill


# Create your models here.

class Profile(models.Model):
    """ Profile Model """
    #user = models.ForeignKey(User, related_name="profile", on_delete=models.CASCADE)
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    image = models.ImageField(upload_to="profiles/")
    image_thumbnail = ImageSpecField(source='image',
                                  processors=[ResizeToFill(300, 300)],
                                  format='WEBP',
                                  options={'quality': 75})
    bio = RichTextField(max_length=2500, null=True, blank=True)
    age = models.FloatField(null=False, default='0')
    weight = models.FloatField(null=False, default='0')

    def __str__(self):
        return str(self.user.username)


@receiver(post_save, sender=User)
def create_user_profile(instance, created, **kwargs):
    """ Create or update the user profile """
    if created:
        Profile.objects.create(user=instance)
