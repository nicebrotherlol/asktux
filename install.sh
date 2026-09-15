#!/bin/bash
echo "Installation-Script for 'asktux' by nicebrotherlol"
echo "This script will modify the 'asktux.py' and move a copy of it."
read -p "Continue? [y/N] " answer
case "${answer,,}" in
	y|yes)
		echo -e "\n Making 'asktux.py' excecuteable..."
		chmod +x asktux.py
		echo -e "\n Copying file..."
		sudo cp asktux.py /usr/local/bin/asktux
		;;
	*)
		echo -e "\n Cancelling..."
		;;
esac
