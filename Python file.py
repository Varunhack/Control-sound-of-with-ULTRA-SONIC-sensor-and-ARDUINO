import pyautogui
import time
import serial
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
#from pen_track2 import main
def remap( x, oMin, oMax, nMin, nMax ):
    
    #range check
    if oMin == oMax:
        print("Warning: Zero input range")
        return None

    if nMin == nMax:
        print ("Warning: Zero output range")
        return None

    #check reversed input range
    reverseInput = False
    oldMin = min( oMin, oMax )
    oldMax = max( oMin, oMax )
    if not oldMin == oMin:
        reverseInput = True

    #check reversed output range
    reverseOutput = False   
    newMin = min( nMin, nMax )
    newMax = max( nMin, nMax )
    if not newMin == nMin :
        reverseOutput = True

    portion = (x-oldMin)*(newMax-newMin)/(oldMax-oldMin)
    if reverseInput:
        portion = (oldMax-x)*(newMax-newMin)/(oldMax-oldMin)

    result = portion + newMin
    if reverseOutput:
        result = newMax - portion

    return result

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
ser = serial.Serial('COM10',9600)

l = [0]

while True:
    x = ser.readline().decode('latin1')
    print(x)
    if x.isnumeric:
        z = int(x)
        z = float(z)
        if z <= 20:
            y = remap(z,0,20,-65.25,0)
            y = float(y)
            print(y)
            volume.SetMasterVolumeLevel(y,None)
            l.append(y)
        elif z > 20:
            volume.SetMasterVolumeLevel(l[-1],None)
#main()
