from comtypes.client import CreateObject
from comtypes.gen import SpeechLib   
# Denna kod fungerar endast för Windows 

engine = CreateObject("SAPI.SpVoice")
stream = CreateObject("SAPI.SpFileStream")
infile = "SLAYER AI small 1.txt"
outfile = "SLAYER AI small 1.wav" 
# Jag testade att göra .mp3 filer på direkten, men filerna som skapades då fungerade inte qlls
stream.Open(outfile, SpeechLib.SSFMCreateForWrite)
engine.AudioOutputStream = stream
f = open(infile, 'r')
theText = f.read()
f.close()
engine.speak(theText)
stream.Close()
