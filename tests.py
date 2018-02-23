import time

import Adafruit_GPIO.SPI as SPI 
import Adafruit_MCP3008
import RPi.GPIO as GPIO 


SPI_PORT = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE)) 





print('begin program for debugging purposes...') 

GPIO.setmode(GPIO.BCM) 
GPIO.setup(17, GPIO.OUT)
while True:
    
    print ('Beginning test 1') 
    for x in range(0,5):
        GPIO.output(17, GPIO.HIGH)
        time.sleep(0.5) 
        GPIO.output(17, GPIO.LOW) 
        time.sleep(0.5) 
    print ('Done with test 1') 

    print ('Beginning test 3')
    for x in range(1,50):
        val = mcp.read_adc(1)
        print(val) 
        if val > 501:
            print ('bright')
        else:
            print ('dark') 
        time.sleep(1.1) 
    print ('Done with test 3')
     
    print ('Beginning test 4')
    for x in range(1,4):
        GPIO.output(18, GPIO.HIGH)
        time.sleep(1.2)
        GPIO.output(18, GPIO.LOW)
        time.sleep(1.2)
    print ('Done with test 4') 

    print ('Beginning test 5')
    for x in range(1,50):
        val = mcp.read_adc(2)
        print(val) 
        if (val > 401):
            GPIO.output(18, GPIO.HIGH)
            time.sleep(1.1)
            GPIO.output(18, GPIO.LOW)
            x = x + 2 
        time.sleep(1.1) 
    print ('Done with test 5') 

    print('Beginning test 6')
    for x in range(1,4):
        GPIO.output(18, GPIO.HIGH)
        time.sleep(1.2)
        GPIO.output(18, GPIO.LOW)
        time.sleep(1.2)
    print('Done with test 5') 

    time.sleep(5) 

