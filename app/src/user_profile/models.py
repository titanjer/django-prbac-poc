from django.db import models
from django.conf import settings

from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User

from django_prbac.models import ValidatingModel, Role, Grant

# Create your models here.


class UserProfile(ValidatingModel, models.Model):

    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                related_name='profile',
                                on_delete=models.CASCADE)

    role_user = models.OneToOneField(Role,
                                     related_name='user',
                                     on_delete=models.CASCADE)

    role_admin = models.OneToOneField(Role,
                                      related_name='admin',
                                      on_delete=models.CASCADE)

    def __eq__(self, other):
        return self.user == other.user and self.role_user == other.role_user \
                and self.role_admin == other.role_admin

    def __repr__(self):
        return 'UserProfile(user={}, role_user={}, role_admin={})'.format(
                self.user, self.role_user, self.role_admin)


@receiver(post_save, sender=User)
def ensure_profile_exists(sender, instance, created, **kwargs):
    if created:
        user_id = instance.id
        role_user = Role.objects.create(name='user_{}'.format(user_id),
                                        slug='u_{}'.format(user_id),
                                        description='user {}'.format(user_id))
        role_admin = Role.objects.create(name='admin_{}'.format(user_id),
                                         slug='a_{}'.format(user_id),
                                         description='admin {}'.format(user_id))
        Grant.objects.create(from_role=role_user, to_role=role_admin)
        UserProfile.objects.get_or_create(user=instance,
                                          role_user=role_user,
                                          role_admin=role_admin, )
