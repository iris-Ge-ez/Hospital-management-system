from email.mime import base
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from .models import User, Director, Doctor, Nurse, Receptionist, HospitalManager, Laboratorist

@receiver(pre_save, sender=User)
@receiver(pre_save, sender=Director)
@receiver(pre_save, sender=Doctor)
@receiver(pre_save, sender=Nurse)
@receiver(pre_save, sender=Receptionist)
@receiver(pre_save, sender=HospitalManager)
@receiver(pre_save, sender=Laboratorist)
def set_username_and_password_callback(sender, instance, *args, **kwargs):
    if User.objects.filter(username=instance.id).exists() or User.objects.filter(username=instance.username).exists():
        print("pass")
        pass
    else:
        last = 0
        try:
            try:
                last_username = int(User.objects.filter(type=instance.type).last().username[-3:])
                base_type = instance.type
            except:
                last_username = int(User.objects.filter(type=instance.base_type).last().username[-3:])
                base_type = instance.base_type
            print(base_type)
        except Exception:
            last_username = 1
            try:
                base_type = instance.type
            except:
                base_type = instance.base_type
        last_username += 1
        new_username = base_type + '/' + str(last_username).zfill(3)
        password = User.objects.make_random_password()
        instance.username = new_username
        instance.is_staff = True
        instance.set_password(password)
        print("--username: ", new_username, "password: ", password)
        print(new_username, password)
        send_mail(instance.email, new_username, password)


def send_mail(email, username, password):
    from django.core.mail import send_mail
    from django.conf import settings

    subject = 'New account created'
    message = 'Your username is: ' + username + '\n' + 'Your password is: ' + password
    from_email = settings.EMAIL_HOST_USER
    to_list = [email]
    send_mail(subject, message, from_email, to_list, fail_silently=False)
    print("successfully sent to: ", email)