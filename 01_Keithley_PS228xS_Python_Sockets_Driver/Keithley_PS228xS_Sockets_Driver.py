#!/usr/bin/python
import socket
import struct
import math
import time

echoCmd = 1


def instrConnect(mySocket, myAddress, myPort, timeOut, doReset, doIdQuery):
    mySocket.connect((myAddress, myPort)) # input to connect must be a tuple
    mySocket.settimeout(timeOut)
    if doReset == 1:
        instrSend(mySocket, "*RST")
    if doIdQuery == 1:
        tmpId = instrQuery(mySocket, "*IDN?", 100)
    return mySocket, tmpId

def instrDisconnect(mySocket):
    mySocket.close()
    return

def instrSend(mySocket, cmd):
    if echoCmd == 1:
        print(cmd)
    cmd = "{0}\n".format(cmd)
    mySocket.send(cmd.encode())
    return

def instrQuery(mySocket, cmd, rcvSize):
    instrSend(mySocket, cmd)
    time.sleep(0.01)
    return mySocket.recv(rcvSize).decode()

def PowerSupply_Connect(mySocket, myAddress, myPort, timeOut, doEcho, doReset, doIdQuery):
    mySocket, myId = instrConnect(mySocket, myAddress, myPort, timeOut, doReset, doIdQuery)
    return mySocket, myId

def PowerSupply_Disconnect(mySocket):
    instrDisconnect(mySocket)
        
def PowerSupply_SetVoltage(mySocket, vLevel):
    sndBuffer = "SOURce:VOLTage {}".format(vLevel)
    instrSend(mySocket, sndBuffer)

def PowerSupply_GetVoltage(mySocket):
    sndBuffer = "SOURce:VOLTage?"
    return instrQuery(mySocket, sndBuffer, 32)

def PowerSupply_SetCurrent(mySocket, iLevel):
    sndBuffer = "SOURce:CURRent {}".format(iLevel)
    instrSend(mySocket, sndBuffer)

def PowerSupply_GetCurrent(mySocket):
    sndBuffer = "SOURce:CURRent?"
    return instrQuery(mySocket, sndBuffer, 32)

def PowerSupply_SetOutputState(mySocket, myState):
    if myState == 0:
        instrSend(mySocket, "OUTP OFF")
    else:
        instrSend(mySocket, "OUTP ON")

def PowerSupply_GetOutputState(mySocket):
    return instrQuery(mySocket, "OUTP?", 16)

def PowerSupply_SetDisplayText(mySocket, myText):
    sndBuffer = "DISP:USER:TEXT \"{}\"".format(myText)
    instrSend(mySocket, sndBuffer)

def PowerSupply_GetDisplayText(mySocket):
    return instrQuery(mySocket, "DISP:USER:TEXT?", 32)




