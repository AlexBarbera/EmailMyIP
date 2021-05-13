import json
import sys
import smtplib, ssl
from requests import get


def send_mail(data):
	context = ssl.create_default_context()

	msg = "Subject: House changed IP!\n\nHouse IP is now {}\n\nBesis".format(data['ip'])

	with smtplib.SMTP_SSL(data['smtp_server'], data['mail_port'], context=context) as server:
		server.login(data['mail_from'], data['mail_passwd'])
		server.sendmail(data['mail_from'], data['mail_to'], msg)

def check_ip(data):
	ip = get(data['ip_check_url']).text
	
	if ip == data['ip']:
		return True

	data['ip'] = ip

	return False


if __name__ == '__main__':
	data = None

	with open(sys.argv[1], 'r') as f:
		data = json.load(f)

	if check_ip(data):
		exit()

	send_mail(data)

	with open(sys.argv[1], 'w') as f:
		f.write(json.dumps(data))
