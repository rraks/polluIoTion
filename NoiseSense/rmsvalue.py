import pyaudio
import wave
import audioop
import math

CHUNK =8192					#1024 #44100 
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

def rec(RECORD_SECONDS):
#	for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
#    		data = stream.read(CHUNK)
    		data = stream.read(CHUNK, exception_on_overflow = False)
#		frames.append(data) 		# 2 bytes(16 bits) per channel
    		rms = audioop.rms(data,2)	#the root-mean-square of the fragment, i.e. ``sqrt(sum(S_i^2)/n)``
# 		print rms			#This (rms) is a measure of the power in an audio signal.
#		peak = 2.8 * rms
#		db = 20 * math.log10(peak)
		db = 20 * math.log10(rms)
		return db			
while True:
	soundlevel = rec(1)
	soundlevel = str(round(soundlevel, 2))
	print soundlevel

stream.stop_stream()
stream.close()
p.terminate()


