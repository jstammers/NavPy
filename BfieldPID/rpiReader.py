#! /usr/bin/env python

import time
import os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
DEBUG = 1

def readadc(adcnum, clockpin, mosipin, misopin, cspin):
    if ((adcnum > 7) or (adcnum < 0)):
        return -1
    GPIO.output(cspin, True)

    GPIO.output(clockpin,False)
    GPIO.output(cspin, False)

    commandout = adcnum
    commandout |= 0x18 # start bit + single-ended bit
    commandout <<= 3 #only need to send the first 5 bits
    for i in range(5):
       
        if (commandout & 0x80):
            GPIO.output(mosipin, True)
        else:
            GPIO.output(mosipin, False)
        commandout <<= 1
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
    adcout = 0
    #read in one empty bit, one null bit and 10 ADC bits
    for i in range(11):
        GPIO.output(clockpin, True)
        GPIO.output(clockpin, False)
        adcout <<= 1
        if (GPIO.input(misopin)):
            adcout |= 0x1
    GPIO.output(cspin,True)

    #drop the first bit since we don't need it
    adcout >>= 1
    return adcout


#pin configuration -  for now these are the default values
SPICLK = 11
SPIMOSI = 10
SPIMISO = 9
SPICS = 8

def read(adcnum,single=True):
    if single:
        return readadc(adcnum,SPICLK,SPIMOSI,SPIMISO,SPICS)

#set up the interface
GPIO.setup(SPICLK,GPIO.OUT)
GPIO.setup(SPIMOSI, GPIO.OUT)
GPIO.setup(SPIMISO,GPIO.IN)
GPIO.setup(SPICS,GPIO.OUT)