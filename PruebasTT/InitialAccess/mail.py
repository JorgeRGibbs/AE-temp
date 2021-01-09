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

#Attach JS

#filename='attachments/test.js'
#fp=open(filename,'rb')
#att = email.mime.application.MIMEApplication(fp.read(),_subtype="js")
#fp.close()
#att.add_header('Content-Disposition','attachment',filename=filename)
#msg.attach(att)

# send via Gmail server
# NOTE: my ISP, Centurylink, seems to be automatically rewriting
# port 25 packets to be port 587 and it is trashing port 587 packets.
# So, I use the default port 25, but I authenticate. 
s = smtplib.SMTP(host='ecorp.local')
#s.starttls()
#s.login('xyz@gmail.com','xyzpassword')
filename = '/home/kali/AE-temp/lib/base/cli/modules/InitialAccess/T1566/001/eml_templates/test.eml'
with open(filename) as f:
	message = f.read()

s.sendmail('wwhite@ecorp.local',['Administrator@ecorp.local'], msg.as_string())
s.sendmail('wwhite@ecorp.local',['Administrator@ecorp.local'], message)

s.quit()
