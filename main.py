import SoilHumidity

SENSORS = [SoilHumidity.getValue]


for sensor in SENSORS:
    print(sensor())