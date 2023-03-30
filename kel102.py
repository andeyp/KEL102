# -*- coding: iso8859-15 -*-

import serial
import time


LoadType = ""
bLoadInit = False

def LoadInit(Type, Port):
    global Load, LoadType, bLoadInit
    LoadType = Type
    bLoadInit = False
    if LoadType == "KEL":
        Load = serial.Serial()
        Load.baudrate = 9600
    else:
        return (False, "Load COM-Port-Init: unknown type!\n")
    Load.port = Port
    Load.bytesize = serial.EIGHTBITS
    Load.parity = serial.PARITY_NONE
    Load.stopbits = serial.STOPBITS_ONE
    Load.timeout = 1
    try:
        Load.open()
        LoadInit = True
        if LoadType == "KEL":
            Load.write("*IDN?\n")
            time.sleep(0.5)
        return (True, "Electrical Load COM-Port initialized. \n")
    except Exception, e:
        return (False, "Electrical Load COM-Port error: {0} Program will be terminated.\n".format(str(e)))
    except:
        return (False, "Electrical Load COM-Port-Init: unknown problem!\n")

# Ausgang Abschalten
def LoadExit():
    global LoadInit
    if LoadType == "KEL":
        Load.write(":INPut OFF\n")
        time.sleep(0.5)
    LoadInit = False
    Load.close()

# Ausgang anschalten
def LoadOn():
    if LoadType == "KEL":
        Load.write(":INPut ON\n")
    time.sleep(0.5)

# Ausgang ausschalten
def LoadOff():
    if LoadType == "KEL":
        Load.write(":INPut OFF\n")
    time.sleep(0.5)

# Konstantspannung einstellen.
def LoadSetCV(dValue):
    if LoadType == "KEL":
        Load.write(":FUNC CV\n")
        Load.write(":VOLT {0}V\n".format(str(dValue)))
        LoadOn()
    time.sleep(0.5)

# Konstantstrom einstellen.
def LoadSetCC(dValue):
    if LoadType == "KEL":
        Load.write(":FUNC CC\n")
        Load.write(":CURR {0}A\n".format(str(dValue)))
        LoadOn()
    time.sleep(0.5)

# Maximale Leistung einstellen.
def LoadSetPower(dValue):
    if LoadType == "KEL":
        Load.write(":POW {0}W\n".format(str(dValue)))
        LoadOn()
    time.sleep(0.5)

# Spannung auslesen.
def LoadGetVoltage():
    if LoadType == "KEL":
        Load.flushInput()
        Load.write(":MEAS:VOLT?\n")
    time.sleep(0.5)
    trys = 10
    while trys >0 and Load.inWaiting() == 0:
        time.sleep(0.05)
        trys -= 1
    if trys > 0:
        rawValue = Load.readline()
        rawValue = rawValue[:-1]
        fltValue = float(rawValue[:-1])
        return (True, fltValue)
    else:
        fltValue = 0.0
        return (False, fltValue)

# Strom auslesen.
def LoadGetCurrent():
    if LoadType == "KEL":
        Load.flushInput()
        Load.write(":MEAS:CURR?\n")
    time.sleep(1)
    trys = 10
    while trys > 0 and Load.inWaiting() == 0:
        time.sleep(0.05)
        trys -= 1
    if trys > 0:
        rawValue = Load.readline()
        rawValue = rawValue[:-1]
        fltValue = float(rawValue[:-1])
        return (True, fltValue)
    else:
        fltValue = 0.0
        return (False, fltValue)

# Power auslesen.
def LoadGetPower():
    if LoadType == "KEL":
        Load.flushInput()
        Load.write("MEAS:POW?\n")
    time.sleep(0.5)
    trys = 10
    while trys > 0 and Load.inWaiting() == 0:
        time.sleep(0.05)
        trys -= 1
    if trys > 0:
        rawValue = Load.readline()
        rawValue = rawValue[:-1]
        fltValue = float(rawValue[:-1])
        return (True, fltValue)
    else:
        fltValue = 0.0
        return (False, fltValue)