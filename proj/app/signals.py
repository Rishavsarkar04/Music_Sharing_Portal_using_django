from django.db.models.signals import pre_delete
from django.dispatch import receiver
from app.models import MusicFile
from django.contrib.auth.signals import user_logged_out,user_logged_in
from django.contrib import messages

@receiver(pre_delete,sender=MusicFile)
def files_delete(sender, instance, using, **kwargs):
    instance.file.delete()
    instance.image.delete()

@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    messages.add_message(request, messages.INFO, 'You Are Logged Out.')

@receiver(user_logged_in)
def on_user_logged_in(sender, request, **kwargs):
    messages.add_message(request, messages.INFO, f'{request.user} Logged In.')
