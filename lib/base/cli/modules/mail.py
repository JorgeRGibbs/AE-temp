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
msg['Subject'] = 'Greetings'
msg['From'] = 'saguaro@lab.local'
msg['To'] = 'Administrator@lab.local'

# The main body is just another attachment
body = email.mime.text.MIMEText("""Hello, how are you? I am fine.
This is a rather nice letter, don't you think?""")
msg.attach(body)

# Attach PDF 
filename='test.pdf'
fp=open(filename,'rb')
att = email.mime.application.MIMEApplication(fp.read(),_subtype="pdf")
fp.close()
att.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(att)

#Attach JS

filename='test.js'
fp=open(filename,'rb')
att = email.mime.application.MIMEApplication(fp.read(),_subtype="js")
fp.close()
att.add_header('Content-Disposition','attachment',filename=filename)
msg.attach(att)

# send via Gmail server
# NOTE: my ISP, Centurylink, seems to be automatically rewriting
# port 25 packets to be port 587 and it is trashing port 587 packets.
# So, I use the default port 25, but I authenticate. 
s = smtplib.SMTP('lab.local')
#s.starttls()
#s.login('xyz@gmail.com','xyzpassword')
s.sendmail('saguaro@lab.local',['Administrator@lab.local'], msg.as_string())
s.quit()