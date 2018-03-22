from django.core.mail import send_mail

def enviar_email():
	send_mail(
	    'Linda',
	    'Fabiano aqui.',
	    'fabio@gmail.com',
	    ['sywrahgabriella@gmail.com'],
	    fail_silently=False,
	)