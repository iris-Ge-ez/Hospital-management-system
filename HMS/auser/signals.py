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
    last = 0
    if instance.base_type == 'DI':
        try:
            last_username = Director.objects.last().username[3:]
        except Exception:
            last_username = "001"
        new_id = 0



# password = User.objects.make_random_password()
# user.set_password(password)
# user.save()

# def send_welcome_email(sender,instance,created, **kwargs):
#     user= instance
#     current_site = get_current_site(request=None)
#     domain = current_site.domain
#     page_url = reverse('set_password')
#     protocol = "http"
#     url = '{protocol}://{domain}/{page_url}'.format(protocol=protocol, domain=domain, page_url = page_url)

#     subject,from_email , to = 'welcome to isow investors team', 'settings.EMAIL_HOST_USER',user.email
#     context =  {'name':user.first_name,'new_username':user.username, 'user_email': user.email , 'url':url}
#     text_content = render_to_string('accounts/welcome_email_template.txt',context)
#     html_content = render_to_string('accounts/welcome_email_template.html', context)

#     msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
#     msg.attach_alternative(html_content, "text/html")
#     msg.send()
#     print("Welcome email sent to user")

# post_save.connect(send_welcome_email, sender=User)


# @receiver(pre_save)
# def generate_password(pre_save, sender, instance, **kwargs):
#     if not instance.id:
#         instance.set_password(User.objects.make_random_password())