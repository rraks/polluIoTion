from CO2Sense import t6713
from PMSense import HPMA115S0
from NoiseSense import Noise

import time


co2Sensor = t6713.T6713()
hpma115S0 = HPMA115S0.HPMA115S0("/dev/ttyUSB0")
hpma115S0.init()
hpma115S0.startParticleMeasurement()


pollution = {}



if __name__ == "__main__":
	while True:

		try:

                	if (hpma115S0.readParticleMeasurement()):
				pollution["pm2.5"] = hpma115S0._pm2_5
                    		pollution["pm10"] = hpma115S0._pm10
		except Exception as e :
			print(e)

		pollution["co2"] = co2Sensor.gasPPM()
		pollution["NoiseLevel"] = Noise.measure()
		print(pollution)
	        time.sleep(1)
