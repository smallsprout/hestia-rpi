#!/usr/bin/env python

import RPi.GPIO as GPIO
from hestiarpi.config import common
import time, logging, threading, socket, errno

def start():
    logging.info("[library.monitor.rpi:start] started")
    _observe_light_module()

def _observe_light_module():
    pass

def get_light_data():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(common.GPIO_LIGHT_OUTPUT_VCC, GPIO.OUT)
    GPIO.setup(common.GPIO_LIGHT_INPUT_DATA, GPIO.IN)
    GPIO.output(common.GPIO_LIGHT_OUTPUT_VCC, GPIO.HIGH)
    return GPIO.input(common.GPIO_LIGHT_INPUT_DATA)

def set_sound_on():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(common.GPIO_ALERT_OUTPUT_VCC, GPIO.OUT)
    GPIO.setup(common.GPIO_ALERT_OUTPUT_DATA, GPIO.OUT)
    GPIO.output(common.GPIO_ALERT_OUTPUT_DATA, GPIO.LOW)
    GPIO.output(common.GPIO_ALERT_OUTPUT_VCC, GPIO.HIGH)

def set_sound_off():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(common.GPIO_ALERT_OUTPUT_VCC, GPIO.OUT)
    GPIO.setup(common.GPIO_ALERT_OUTPUT_DATA, GPIO.OUT)
    GPIO.output(common.GPIO_ALERT_OUTPUT_DATA, GPIO.HIGH)
    GPIO.cleanup((common.GPIO_ALERT_OUTPUT_VCC, common.GPIO_ALERT_OUTPUT_DATA))
