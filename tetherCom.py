import serial
import io
import msgpack
import queue
import RPi.GPIO as GPIO

yamHole = serial.Serial('/dev/serial0', 115200)  # open serial port

yamFarmer = msgpack.Unpacker(raw=False)

yamQueue = queue.Queue()

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(11, GPIO.OUT)


def sendYam(msg):
    msg = msgpack.packb(msg, use_bin_type=False)
    GPIO.output(11, 1)
    yamHole.write(msg)
    yamHole.flush()
    GPIO.output(11, 0)


def grabNextYam():
    if (not yamQueue.empty()):
        return yamQueue.get()
    else:
        return None


def harvestYams():
    yamFarmer.feed(yamHole.read())
    for yam in yamFarmer:
        yamQueue.put(yam)


def shutdownYamProduction():
    GPIO.cleanup(11)
