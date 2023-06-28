from django.shortcuts import render

# Create your views here.
import secrets
import string

def generateur(request):
	alphabet = string.ascii_letters + string.digits + string.punctuation
	pswd_len = 20
	pswd = ''

	for i in range(pswd_len):
		pswd += ''.join(secrets.choice(alphabet))

	return render(request, 'generateur/password.html', {'password': pswd})


