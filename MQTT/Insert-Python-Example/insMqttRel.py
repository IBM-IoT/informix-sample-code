""" Uses db1.sql To insert into a relational table
"""

from json import JSONEncoder
from datetime import datetime
import paho.mqtt.client as mqtt


NUMINS = 20000

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
    ct = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-1]
    msg = JSONEncoder().encode({
        "sensor_id":"4",
        "tstamp" : ct,
        "d" : {"col4": "king bob"}
        })
    msgstr = '{  "col1":%d, "col2" :%d, "col3":"%s"}'  % (i, i+1,"bob")

    (result, mid) = client.publish("db1.tab1", msgstr, qos=0)
    if result != mqtt.MQTT_ERR_SUCCESS:
        print("Error Publish: ", i)

    if  (i % 1000) == 0:
        print("I: ", i)


client.loop_forever()
