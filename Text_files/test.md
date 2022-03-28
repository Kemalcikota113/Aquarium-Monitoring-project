# Agenda for testing Fish feeder


**Need :**

The need of this projects comes from the group members own need to be able to feed the fish and monitor the generall state of the aquarium without beeing at home.

**Requirments :**

- As a potentiall user of this product i want to be able to feed the fish while not at home
- As a user of this product i want to be able to read information about the aquarium in a way that would be easy to understand.
- As a customer i also want the possibillity to look at about the aquarium in a fast, easy and simple way at home (without relying on the IoT).

---

The group has tested the different components using exploring techniques that are within a reasonable realm of what the components needs to acheive. The group will refer to the [requirements.md](https://gitlab.lnu.se/1dt308/student/grupp-4---aquarium-monitoring/project/-/blob/main/Text_files/Requirements.md) documentation when reflecting uppon the testing made.

The group tests the product to see how the product feels to operate from the customers perspective.

1. The product is set up and running on idle properly.
2. Fill the fish tank reservoir
3. The USB is connected
4. VSCode is started
5. Adafruit MQTT broker is started
6. Fill in your wifi configuration in the "main.py" file.
7. Fill in your Adafruit account information.
8. On the dashboard, press "Feed".
9. We can see that the screw is dispensing food and the dashboard tells us that the "motor stepped".
10. The dashboard tells us the information from the ranging sensor and temperature sensor, this beeing depth of the water, temperature and humidity.
11. The LCD tells us the information from the temperature sensor.
12. The RGB-LED emits light

**Customers feedback :** 

Positive : The Adafruit interface is easy to read and use and gives a good representation not only of current data but also historical data that is usefull when seeing how the temperature changes during different events or times of day.

Positive : The main function of the fish works great. The fish were fed during christmas holidays and survived and there were plenty of food left in the tank so the size of it is appropriate.

Negative : Uppoon using and operating the device the customers states that the RGB-LED isn't necessary as the LCD function does a better job at showing the information necessary for the user. It is also annoying during night time because it emits a strong light which lights up the whole room and makes it sometimes harder to sleep.

Negative : The humidity from the DHT-11 sensor is deemed irrelevant as the nature of a aquarium even above the surface is very humid.

**measures taken :**

What does the group need to change?

- Remove the RGB-LED
- Dissable the humidity function from the DHT-11

How will the group change this?

Fortunetly the criticism given isn't hard to fix, because the RGB-LED isn't usefull at all we simply disconnect it and exclude it from the project completely because it does more bad then good. The humidity values are also easy to remove but because the temperature is important we will only remove the humidity function from the code and not remove or change any sensors.
