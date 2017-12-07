"""  No database should exist.  This inserts into a collection so it will
     create the database and table
"""
from datetime import datetime
import paho.mqtt.client as mqtt


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

insertCollection()

for i in range(1, NUMINS + 1):
    ct = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-1]
    msgstr = '{  "sensor_id":%d, "tstamp" : "%s",  "d" : { "col4": "king bob"}  }'  % (i, ct)

    (result, mid) = client.publish("mongo_db.collection1", msgstr, qos=1)
    if result != mqtt.MQTT_ERR_SUCCESS:
        print("Error Publish: ", i)

    if  (i % 1000) == 0:
        print("I: ", i)


client.loop_forever()
