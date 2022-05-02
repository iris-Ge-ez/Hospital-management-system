from django.db.models.signals import post_save, pre_save
from .models import User

user = get_user_model() 
password = User.objects.make_random_password()
user.set_password(password)
user.save()

def send_welcome_email(sender,instance,created, **kwargs):
    user= instance
    current_site = get_current_site(request=None)
    domain = current_site.domain
    page_url = reverse('set_password')
    protocol = "http"
    url = '{protocol}://{domain}/{page_url}'.format(protocol=protocol, domain=domain, page_url = page_url)

    subject,from_email , to = 'welcome to isow investors team', 'settings.EMAIL_HOST_USER',user.email
    context =  {'name':user.first_name,'new_username':user.username, 'user_email': user.email , 'url':url}
    text_content = render_to_string('accounts/welcome_email_template.txt',context)
    html_content = render_to_string('accounts/welcome_email_template.html', context)

    msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
    msg.attach_alternative(html_content, "text/html")
    msg.send()
    print("Welcome email sent to user")

post_save.connect(send_welcome_email, sender=User)


@receiver(pre_save)
def generate_password(pre_save, sender, instance, **kwargs):
    if not instance.id:
        instance.set_password(User.objects.make_random_password())