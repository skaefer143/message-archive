from django.db import models
from model_utils.managers import InheritanceManager
from phonenumber_field.modelfields import PhoneNumberField


class Person(models.Model):
    """ Represents a person. Messages link to these people. """
    name = models.CharField(max_length=128, blank=False, null=False)
    phone_num = PhoneNumberField(blank=True)
    facebook_name = models.CharField(max_length=128)


class Message(models.Model):
    """ Base class for a message. All message types should subclass from this. """
    sender = models.ForeignKey(Person, related_name='sender_messages', on_delete=models.CASCADE)
    recipient = models.ForeignKey(Person, related_name='recipient_messages', on_delete=models.CASCADE)
    date_sent = models.DateTimeField(null=False, blank=False)
    body = models.TextField()

    objects = InheritanceManager()


class FacebookMessage(Message):
    """ Represents a facebook message from one user to another. Can reference photos, a message, or a video call. """
    TYPE_GENERIC = ('generic', 'Generic')
    TYPE_CALL = ('call', 'Call')
    TYPE_SHARE = ('share', 'Share')

    TYPE_CHOICES = (
        TYPE_GENERIC,
        TYPE_CALL,
    )
    message_type = models.CharField(choices=TYPE_CHOICES, max_length=32)
    # Used by Facebook Messages. An external link attached to a message.
    external_share_url = models.CharField(max_length=512)
    call_duration = models.PositiveBigIntegerField(null=True, blank=True)  # Only filled in when message type = call
    # Stores the amount of seconds of a call. PositiveBigIntegerField should be enough lol


class TextMessage(Message):
    """ Stores the text message data backed up by the SMS Backup & Restore app on Android. """
    # Don't really have any extra stuff here right now, oh well just in case.
    pass


class Photo(models.Model):
    """ Represents a photo stored externally (on a cdn, for instance) or a filepath locally on the server media folder.
    """
    image_name = models.CharField(max_length=512)
    internal_image_url = models.CharField(max_length=512)  # Stored in filepath on server
    external_image_url = models.CharField(max_length=512)  # Stored in cdn
