#!/bin/bash
#service network-manager stop
service networking stop
killall wpa_supplicant
#killall dhclient
ifconfig wlan0 down
iwconfig wlan0 essid ardrone2_034886
ifconfig wlan0 up
