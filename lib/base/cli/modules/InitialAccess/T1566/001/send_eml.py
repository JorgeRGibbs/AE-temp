from sploitkit import *
import sys
import os.path
import smtplib

'''
class send_eml(Module):
	""" Send emails with a pre made eml file. 

	Author:  your name (your email)
	Version: 1.0
	"""

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


if len(sys.argv) <= 2:
	print('Usage:')
	print('  $ python ' + sys.argv[0] + ' mailfrom rcptto <emlfile>')
	print
	print('Parameter:')
	print('  mailfrom: MAIL FROM address.')
	print('  rcptto:   RCPT TO address.')
	print('  emlfile:  Message file in eml format. When emlfile is not specified, an empty message will be send.')
	print
	print('Example:')
	print('  $ python ' + sys.argv[0] + ' mailfrom@example.com rcptto@example.com mail.eml')
	sys.exit(0)

server = '10.10.1.10'
port = 25
mailfrom = sys.argv[1]
rcptto = sys.argv[2].split(',')

message = ''
if len(sys.argv) >= 4:
	filename = sys.argv[3]
	if not os.path.isfile(filename):
		print('File "' + filename + '" not found.')
		sys.exit(0)
	with open(filename) as f:
		message = f.read()

smtp = None
try:
	smtp = smtplib.SMTP(server,port)
	smtp.sendmail(mailfrom,rcptto,message)
except Exception as e:
	print('Failed to send mail.')
	print(str(e))
else:
	print('Succeeded to send mail.')
finally:
	if smtp != None:
		smtp.close()
'''