import secrets
import string

def generator():
	alphabet = string.ascii_letters + string.digits + string.punctuation
	pswd_len = 20
	pswd = ''

	for i in range(pswd_len):
		pswd += ''.join(secrets.choice(alphabet))
	print(pswd)

if __name__ == '__main__':
    generator()
