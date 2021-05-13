import json
import sys


def send_mail(data):
	pass

def check_ip(data):
	pass

if __name__ == '__main__':
	data = None

	with open(sys.argv[1], 'r') as f:
		data = json.load(f)

	if check_ip(data):
		exit()

	send_mail(data)

	with open(sys.argv[1], 'w') as f:
		f.write(json.dumps(data))
