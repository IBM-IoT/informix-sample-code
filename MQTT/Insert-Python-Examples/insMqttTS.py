"""  Uses iot_db.sql to insert into a vti timeseries table
"""
from json import JSONEncoder
from datetime import datetime
import paho.mqtt.client as mqtt
import time

NUMINS = 10

def on_publish(client, userdata, mid):
    """ on_publish:
    """
    print("MID Published: ", mid)
    if mid == NUMINS:
        client.disconnect()


client = mqtt.Client(protocol=mqtt.MQTTv31)
client.on_publish = on_publish

client.connect("127.0.0.1", 27883)

client.loop_start()


for i in range(1, NUMINS + 1):
    #currentTimeStr = datetime.now().strftime("%Y-%m-%dT%H:%M:%S.%f")[:-1]

    currentTimeNow = time.time()
    currentTimeInt = int(currentTimeNow*1000)
    currentTimeStr = datetime.fromtimestamp(currentTimeNow).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-1]

    msgstr = '{  "id":1, "desc":"description data",  "ts" : {"$date":%s},  "reading" : {"col4": "king david" } }'  % (currentTimeInt)
    msgstr = '{  "id":1, "desc":"description data",  "ts" : {"$date":%s},  "col1"  : "king bob", "col2":"King fred"  }'  % (currentTimeInt)

    msgstr = '{  "id":1,  "ts" : {"$date":%s},  "col1"  : "king bob", "col2":"king fred"  }'  % (currentTimeInt)

    #msgstr = '{  "id":1,  "ts" : "%s",  "col1"  : "king bob"  }'  % (currentTimeStr)

    print("Publish ",msgstr)
    print("   TimeNow:",currentTimeNow)
    print("   TimeInt:",currentTimeInt)
    print("   TimeStr:",currentTimeStr)
    (result, mid) = client.publish("iot.iot_data_ts", msgstr, qos=1)
    if result != mqtt.MQTT_ERR_SUCCESS:
        print("Error Publish: ", i)

    if  (i % 1000) == 0:
        print("I: ", i)


client.loop_forever()
