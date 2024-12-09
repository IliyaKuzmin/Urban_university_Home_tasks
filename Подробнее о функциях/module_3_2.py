#!/usr/bin/python3
default_sender="university.help@gmail.com"
require=["@",".com",".ru",".net"]
# email => bool 'is email corect?'
def check_email (email):
	include=0
	for req in require:
		if req in email: include=include+1
	if include==2:
		return True
	else: return False
def send_email(message,recipient,sender=default_sender):
	all_emails_correct=False
	all_emails_correct=check_email(recipient)
	if sender!=default_sender:
		all_emails_correct=check_email(sender)
	if all_emails_correct:
		if recipient==sender:
			print("Нельзя отправить письмо самому себе!")
		elif sender!=default_sender:
			print("НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо успешно отправлено с адреса",sender,"на адрес",recipient,".")
		else: print("Письмо успешно отправлено с адреса",sender,"на адрес",recipient,".")
	else: print("Невозможно отправить письмо с адреса",sender,"на адрес",recipient,".")
# Поскольку все параметры функции позиционные send_email(сообщение,получатель,отправитель) 
# для задания другого отправителя просто достаточно указать его адрес третьим параметром данной функции
send_email("Message for testing connection","vasyok1337@gmail.com")
send_email("Message for testing connection","vasyok1337@gmail.com","university.info@gmail.com")
send_email("Message for testing connection","vasyok1337@gmail.bk")
send_email("Message for testing connection","vasyok1337@gmail.com","vasyok1337@gmail.com")