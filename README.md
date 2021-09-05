# Control-sound-of-with-ULTRA-SONIC-sensor-and-ARDUINO
Here we are going to use arduino and ultra sonic sensor to control your pc's sound.
# Lets get started

First is first.Before starting all this make sure to you know about arduino and python and don't just copy the code and paste and show off because you will be learning zero.
- Step one : Make the connection of the arduino board according to the image
- Step two : Upload the code which is present in the file **Ardunio.ino**
- Step three : Open the python file and the COM10 with the COM number your using in the file **Don't Change anything else**  
 `ser = serial.Serial('COM10',9600)`
- Step four : Keep your arduino connected to your pc and ultra sonic sensor facing towards the ceiling.And run the Python file.<br>
<br>
Observe that when your hand is 20 cm above your sensor the volume is full and the closer you start bring your hand towards thee sensor the volume starts decreasing.To set the volume kepp the hand at that position for 2-3 sec and pull your hand horzontally. 
