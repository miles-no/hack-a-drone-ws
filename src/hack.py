import RPi.GPIO as GPIO
import time
import os

GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO23
GPIO.setup(24, GPIO.OUT)  #LED to GPIO24

GPIO.setup(25, GPIO.OUT)  #LED to GPIO25
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP) #Button to GPIO26


def Connect():
    try:
        while True:
             button1 = GPIO.input(23)
             button2 = GPIO.input(26)
             if button1 == False:
                 os.system('sudo sh /home/pi/drone-hack/join_network.sh')
                 CheckConnection()
             elif button2 == False:
                 GPIO.output(25, True)
                 print('Powering off...')
                 os.system('sh /home/pi/drone-hack/power_off.sh')
             else:
                 GPIO.output(24, False)
                 GPIO.output(25, False)
    except:
        print('Error')
        GPIO.cleanup()

def CheckConnection():
     print('Checking connection...')
     while True:
        GPIO.output(24, True)
        ssid = os.popen("iwconfig wlan0 \
                | grep 'ESSID' \
                | awk '{print $4}' \
                | awk -F\\\" '{print $2}'").read()
        if ssid.startswith('ardrone') == True:
             time.sleep(3.0)
             GPIO.output(24, True)
             break
        else:
             GPIO.output(24, False)
             time.sleep(1.0)

     print("ssid: " + ssid)
        
Connect()
