# Denna kod fungerar endast för Windows 
from comtypes.client import CreateObject  

engine = CreateObject("SAPI.SpVoice")
stream = CreateObject("SAPI.SpFileStream")
from comtypes.gen import SpeechLib 

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
