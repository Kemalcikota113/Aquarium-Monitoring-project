# Software requirments and guide
Group members: Emad Ali, Kemal Cikota, Anas Mohammed, Yousef Mohammad

Program: Master of science in software technology and technical mathematics

Course: 1DT902

Supervisor/Teacher : Fredrik Ahlgren and Lars Karlsson

___

## Software needed
* VSCode (And PyMakr extension)
* Adafruit
* 360Fusion

___

## Software set-up guide

### VSCode (And PyMakr extension)

1. Download VSCode [Here](https://code.visualstudio.com/download) and follow the installation process, choose the presets and settings to your liking.

2. Once in VsCode open the "Extensions" menu on the far left and search for "pymakr" and click "install". A menu on the bottom of the window should pop up. If a terminal opens up when pressing "Pymakr Console" it works.
    * NOTE : A restart of VSCode might be necessary after installing pymakr as the pymakr menu sometimes doesen't pop up.

![title](/Images/VsCode.jpg)

3. Create a folder called "Project" and in this folder you will create a file called "Main.py" and another folder called "lib"

### 360Fusion

1. Download 360Fusion [Here](https://www.autodesk.com/products/fusion-360/personal), the free version of 360Fusion is sufficient for this project. An account is also needed to start a download. Follow the installation client.

2. Once the installation process is done a "Team" must be created which is simillar to a repo in git. There your modelling will be made

3. Because the modelling is very individuall based on preferances and what printer is beeing used this will not be shown here.

### Adafruit IO

1. Create an account on Adafruit [Here](https://accounts.adafruit.com/users/sign_up).

2. Once an account is created and verified you will get introduced to the dashboard, here you will want to open up "Feeds" that will be on the top menu. In feeds you will press "New Feed", in this project you will need 3 feeds, one per parameter in this project ; One feed for the temperature sensor, ranging sensor and one for controlling the stepper motor.

3. Once this is done go back to "Dashboard" and create a new dashboard, it can be called anything that suits the project for example "Pycom_IoT". Go in your new dashboard and here you will create your widgets for visualising the data given by the sensors. This step is much down to personal preference but you will need atleast one widget per sensor.

    **3.1**

    Press the "Dashboard settings" wheel in the top right corner and press "create New Block".

    **3.2**

    In here you can choose any preset you want. We will show a line chart for the temperature sensor but anything can be used, for example a gauge.

    **3.3**

    Once you have chosen a preset you need to connect a feed, we will connect the temperature as an example.

    **3.4**

    When a feed is chosen you will get asked to customize your widget. Here you can for example put a name, choose labels for the Y and X-Axis and choose the time frame of the chart. 

    **3.5**

    Repeat this for every sensor, make sure it looks somewhat pleasing so it's easy to read.

4. After everything is configured in Adafruit you need to open VsCode and do some configurations there. Go in the github [Repository](https://github.com/pycom/pycom-libraries/tree/master/lib) and download the "mqtt.py" file.

5. Put the "mqtt.py" file in your "lib" folder and in "Main.py" and change the following lines (the lines that have comments in them). :

```
# Wireless network
WIFI_SSID = "Your network" #Network Name
WIFI_PASS = "Your Password" #Password for network


# Adafruit IO (AIO) configuration
AIO_SERVER = "io.adafruit.com"
AIO_PORT = 1883
AIO_USER = "Your Username in Adafruit" #Username
AIO_KEY = "Your AIO key in adafruit" #AIO Key
AIO_CONTROL_FEED = "username/feeds/Stepper" #stepper feed
AIO_TEMP_FEED = "username/feeds/temperature" #temperature feed
AIO_RANGE_FEED = "username/feeds/Ranging" #Ranging feed
```
