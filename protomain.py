import pollut_pb2
from CO2Sense import t6713
from PMSense import HPMA115S0
from NoiseSense import Noise

import time

co2Sensor = t6713.T6713()
hpma115S0 = HPMA115S0.HPMA115S0("/dev/ttyUSB0")
hpma115S0.init()
hpma115S0.startParticleMeasurement()

decryption = {}


pollut_level = pollut_pb2.pollution()					# ProtoBuf object

decrypt = pollut_pb2.pollution()					# ProtoBuf object to store the decrypted message

pollut_level.CO2 = 0
pollut_level.NOISELEVEL = 0.0
pollut_level.PM2_5 = 0
pollut_level.PM10 = 0

if __name__ == "__main__":
	while True:

		try:
			if (hpma115S0.readParticleMeasurement()):
				pollut_level.PM2_5 = hpma115S0._pm2_5
				pollut_level.PM10 = hpma115S0._pm10
			pollut_level.NOISELEVEL = float(Noise.measure() )
			pollut_level.CO2 = co2Sensor.gasPPM()
		except Exception as e :
			print(e)
		
		protoMsg = pollut_level.SerializeToString()		# Encrypting object pollution to ProtoBuf
		print protoMsg
		print "Decoded ProtoBuf message"
		decrypt.ParseFromString(protoMsg)
		decryption["CO2"] = str(decrypt.CO2)		#|
		decryption["Noise"] = round(decrypt.NOISELEVEL,2) 		#|
		decryption["PM2.5"] = decrypt.PM2_5 			#]- Decrypting the ProtoBuf message
		decryption["PM10"] = decrypt.PM10			#|
		print (decryption)					#|
		time.sleep(1)

