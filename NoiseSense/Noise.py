import pyaudio
import wave
import audioop
import math
import signal
import sys

CHUNK = 44100 					#8192#1024 #44100 
FORMAT = pyaudio.paInt16 			#paInt8
CHANNELS = 1
RATE = 44100 					#sample rate
p = pyaudio.PyAudio()

stream = p.open(
	format = FORMAT,
	channels = CHANNELS, 
	rate = RATE,
	frames_per_buffer = CHUNK,
	input_device_index = 2,
	input = True)

def signal_handler(signal, frame):	
	stream.stop_stream()
	stream.close()
	p.terminate()
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

def rec(RECORD_SECONDS):
	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    		data = stream.read(CHUNK, exception_on_overflow = False)
    		rms = audioop.rms(data,2)	#the root-mean-square of the fragment, i.e. ``sqrt(sum(S_i^2)/n)``
		db = 20 * math.log10(rms)
		return db			
def measure():
	while True:
		soundlevel = rec(1)
		soundlevel = str(round(soundlevel, 2))
		return soundlevel


