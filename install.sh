#!/bin/bash

RED='\033[0;31m'
GRN='\033[0;32m'
YLL='\033[1;33m'
NC='\033[0m' # No Color
OSADDITIONS="git python-pip python3-pip mingw-w64 librust-vcpkg-dev"
UN=$(ps -o user= $(ps -o ppid= $(ps -o ppid= $(ps -o ppid= $PPID))))


if [[ $(id -u) != 0 ]]; then
	echo -e "\n[!] El script debe correrse como root!\n\n"
	#echo -e "\n[!] Setup script needs to run as root\n\n"
	exit 0
fi

prompt (){
	while true; do
	    read -p "$1 [Y/n] " yn
	    case $yn in
	        [Yy]* ) ANSWER=1; break;;
	        [Nn]* ) ANSWER=-1; break;;
	        * ) echo "Opción no valida...";;
	    esac
	done
}

#Actualizar sistema?
prompt "Quieres actualizar el sistema antes de continuar?"
#prompt "Update system before continuing?"
if [ "$ANSWER" == "1" ]; then
	sudo apt-get -q update && sudo apt-get -qq upgrade 
	echo "[+]Done"
fi

echo -e "${YLL}[+]Instalando dependencias${NC}"
#echo -e "${YLL}[+]Installing dependencies${NC}"
sudo apt-get -qq install $OSADITIONS
#ASSETS
cd ./lib/base/aux/
echo -e "${YLL}[+]Instalando TransportC2${NC}"
#echo -e "${YLL}[+]Installing TransportC2 /lib/base/cli/aux/transportc2${NC}"
git clone https://github.com/todmephis/transportc2.git #./lib/base/cli/aux/transportc2
cd transportc2/install
sudo chmod +x setup.sh
./setup.sh

cd ../../
echo -e "${YLL}[+]Instalando JS2PDFInjector${NC}"
#echo -e "${YLL}[+]Installing JS2PDFInjector /lib/base/cli/aux/JS2PDFInjector${NC}"
git clone https://github.com/cornerpirate/JS2PDFInjector.git #./lib/base/cli/aux/JS2PDFInjector

echo -e "${YLL}[+]Instalando sploitkit${NC}"
#echo -e "${YLL}[+]Installing sploitkit${NC}"
sudo -u $UN pip3 install sploitkit > /dev/null
