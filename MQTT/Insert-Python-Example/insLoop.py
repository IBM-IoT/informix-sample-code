import paho.mqtt.client as mqtt

import json
import pprint
from datetime import datetime 
from json import JSONEncoder

NUMINS = 20000

def on_publish(client, userdata, mid):
    """ on_publish:
    """
    print("MID Published: ", mid)
    if mid == NUMINS:
        client.disconnect()



client = mqtt.Client(protocol=mqtt.MQTTv31)
client.on_publish = on_publish

client.connect("127.0.0.1", 27883) # 10.0.68.69

client.loop_start()

for i in range(1,NUMINS + 1):
   ct = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")[:-1];
   msg = JSONEncoder().encode( {  
      "sensor_id":"4",
      "tstamp" : ct,
      "d" : { "col4": "king bob"}  
   } )
   msgstr =  '{  "sensor_id":%d, "tstamp" : "%s",  "d" : { "col4": "king bob"}  }'  % (i,ct)
   #msg = JSONEncoder().encode(msgstr)

   (result,mid) = client.publish("wd.sensors_vti", msgstr,qos=0)
   #print "Result, mid: ", result,mid
   if ( result != mqtt.MQTT_ERR_SUCCESS) :
         print ("Error Publish: ", i)

 
   #client.loop(5.0, 1000) 
   #client.publish("wd.sensors_vti_col", msg)
   #print "JSON: " + json.dumps(msg,sort_keys=True,indent=4)

   if ( (i % 1000) == 0 ):
      print ("I: " , i) 
      #time.sleep(.5)


client.loop_forever()
