from django.db.models.signals import pre_delete
from django.dispatch import receiver
from app.models import MusicFile

@receiver(pre_delete,sender=MusicFile)
def files_delete(sender, instance, using, **kwargs):
    instance.file.delete()
    instance.image.delete()
