
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'poc_prbac.settings')
django.setup()


from django_prbac.models import Role

userreport_read = Role.objects.get(slug='record') \
                              .instantiate({'record': 'userreport',
                                            'action': 'read'})
userreport_write = Role.objects.get(slug='record') \
                               .instantiate({'record': 'userreport',
                                             'action': 'write'})

# check record permission for user
assert Role.objects.get(slug='u_2').has_privilege(userreport_read) is True
assert Role.objects.get(slug='u_2').has_privilege(userreport_write) is True

assert Role.objects.get(slug='u_3').has_privilege(userreport_read) is True
assert Role.objects.get(slug='u_3').has_privilege(userreport_write) is True

assert Role.objects.get(slug='u_4').has_privilege(userreport_read) is True
assert Role.objects.get(slug='u_4').has_privilege(userreport_write) is False


# check group admin permission for user
group_infra = Role.objects.get(slug='g_infra')
group_fintech = Role.objects.get(slug='g_fintech')

assert Role.objects.get(slug='a_2').has_privilege(group_infra) is True
assert Role.objects.get(slug='a_2').has_privilege(group_fintech) is True
assert Role.objects.get(slug='a_3').has_privilege(group_fintech) is False
assert Role.objects.get(slug='a_4').has_privilege(group_fintech) is False

print('Test Successfully!')
