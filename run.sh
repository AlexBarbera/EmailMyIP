#! /bin/bash


while :
do
	python -m smtpd -c DebuggingServer -n localhost:1025 &

	pid_server=$!

	~/venv/bin/python send_mail.py personal/config.json

	kill -9 $pid_server

	sleep 3600
done
