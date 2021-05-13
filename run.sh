#! ~/venv/bin/python


while :
do
	sudo python -m smtpd -c DebuggingServer -n localhost:1025

	pid_server=$!

	python send_mail.py config.json

	sudo kill -9 $pid_server

	sleep 3600
done
