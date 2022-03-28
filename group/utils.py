from django.core.mail import send_mail


def send_activation_code(email, code, status):
    if status == 'register':
        send_mail(
            'Активация аккаунта',
            f"Код активации: {code}",
            'rica_project@admin.com',
            [email],
            fail_silently=False
        )