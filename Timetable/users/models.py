import uuid
from django.db import models
from django.conf import settings
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser, Group
from django.utils.encoding import python_2_unicode_compatible
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


@python_2_unicode_compatible
class User(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    # 自己关注的对象, following 是子表
    following = models.ManyToManyField('self')
    # 头像
    portrait = models.ImageField(upload_to='usericon', default='临时头像.jpg')

    def follow(self, user: 'User'):
        self.following.add(user)

    def __str__(self):
        return self.username


class UserGroup(Group):
    pass

    class Meta:
        # proxy = True
        verbose_name_plural = "UserGroup"

    def __str__(self):
        return f"Group({self.name})"


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)
