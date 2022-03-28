# Hardware requirments and guide
Group members: Emad Ali, Kemal Cikota, Anas Mohammed, Yousef Mohammad

Program: Master of science in software technology and technical mathematics

Course: 1DT902

Supervisor/Teacher : Fredrik Ahlgren and Lars Karlsson
___

## Hardware needed

- Pycom LoPy4
- Breadboard
- Cables (male and female)
- 9V battery (And AC/DC adapter cable for power supply)
- Power supply (HW-131)
- Stepper motor (28BYJ-48)
- Stepper motor driver (ULN2003)
- 16x2 LCD display (with ic2 interface adapter, PCF8574T)
- Ultrasonic ranging sensor (HC-SR04)
- Digital temperature sensor (DHT-11 with integrated resistance)
- 3x 560 Ohm resistor
___

## Wireing Guide

### Motor :

1. Connect the battery to the Power supply (HW-131) and make sure to press the button to cut the power out to make the circuits safer to handle.
2. Connect the stepper motor (28BYJ-48) to the driver assigned female socket on the driver (ULN2003)

    Furthermore connect the driver to the pycom in the following way : 

    IN4 ----> P11

    IN3 ----> P10

    IN2 ----> P9

    IN1 ----> P8
3. Change the fuse on the driver to handle 5V power and connect the positive and negative side to the power supply accordingly

    It should look something like this :
    ![](/Images/Motor.jpeg)                                 




### LCD

1. Thanks to the Ic2 adapter on the backside of the LCD we only need the LCD, 4 Male/Female cables and our pycom.
2. Connect the pycom to the LCD in the following way :

    GND ----> GND

    VCC ----> VIN(5V)
    
    SDA ----> P9
    
    SCL ----> P10






1                     |2                   |                  
:-------------------------:|:-------------------------:|
| ![](/Images/LCD.jpeg) | ![](/Images/LCD2.jpg) |

### Supersonic ranging sensor

1. For this application a bread board is needed as a pull-down resistor method is needed.

2. Simplified way to connect the sensor to the Pycom : 

    trig --> Resistor --> P20

    VCC ---> Breadboard --> VIN(5V)

    Echo --> Resistor --> P21

    GND --> GND



1                     |2                   |3                   
| :-------------------------:|:-------------------------:|:-------------------------:|
![](/Images/Supersonic_1.jpg)  | ![](/Images/Supersonic_2.jpg) | ![](/Images/Supersonic_3.jpg)  |


### Temperature sensor

1. Because the temperature sensor has integrated resistance it can be directly wired to the pycom.

    Negative ("-") ----> GND

    Positive ("+") ----> 3v3

    OUT ----> P23

    It should look like this:
    ![title](/Images/Temperature.jpeg)
