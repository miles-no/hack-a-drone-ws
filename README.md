# hack-a-drone WS @ MilesCamp 2019

Welcome to the hack-a-drone WS!

## Getting Started

### Booting the Pi

First we need to insert the SD-card from which the Pi's will load the OS (NOOBS/Raspbian). The card slot is found on the back of the Pi's (opposite of the USB-ports).

The simplest way to power the Pi is through the usb-micro port. Insert the provided USB-cable into your computer, or external power supply*, and the Pi.

  (* the Pi needs about 5v and 1ah to power on, more if you have lots of stuff connected to it.)

### Connecting to the Pi

In this workshop we are going to communicate with the Pi's using SSH and the ethernet port (eth0).  In order to do this we need to enable internet sharing on our local machines (and ssh on the Pi's, but that's already taken care off).

#### Enable internet sharing

##### Mac
Follow the first steps in [this](https://medium.com/@tzhenghao/how-to-ssh-into-your-raspberry-pi-with-a-mac-and-ethernet-cable-636a197d055) guide.
Stop when you get to the point with the terminal.

##### Windows
Follow the steps in the answer in the following [link](https://answers.microsoft.com/en-us/windows/forum/windows_10-networking/internet-connection-sharing-in-windows-10/f6dcac4b-5203-4c98-8cf2-dcac86d98fb9)

##### Linux
¯\\_(ツ)_/¯

#### Testing SSH
In your favorite Terminal type:

```

ᐅ ssh pi@raspberrypi.local

```

Hopefully you'll get prompted to accept the Pi as a known host and eventually asked for the password to login in. (default is 'raspberry')

```
ᐅ ssh pi@raspberrypi.local

pi@raspberrypi.local's password: 

pi@raspberrypi:~ $ 

```

If your terminal is showing the above output, you're all set! Horray!

#### Assignment one

We're now ready to go work, head over to [step 1](./step1.md) for the next instructions.

```
      ____
    ,'   Y`.
   /        \
   \ ()  () /
    `. /\ ,'
8====| "" |====8
     `LLLU'

```