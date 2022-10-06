from MQTTLib import AWSIoTMQTTClient
from network import WLAN
import time
import config
import pycom
from mqtt import MQTTClient
import socket
import machine


import config
import json
from MQTTLib import AWSIoTMQTTShadowClient
from MQTTLib import AWSIoTMQTTClient

from network import MDNS
MDNS.init()
MDNS.set_name(hostname ="pycom", instance_name="pycom")
MDNS.add_service("_http",MDNS.PROTO_TCP, 80)
MDNS.add_service("_telnetd", MDNS.PROTO_TCP, 23)

# Connect to wifi
# wlan = WLAN(mode=WLAN.STA)
# wlan.connect(config.WIFI_SSID, auth=(None, config.WIFI_PASS), timeout=5000)
# while not wlan.isconnected():
#     time.sleep(0.5)
# print('WLAN connection succeeded!')

# Connect to wifi to get time
wlan = WLAN(mode=WLAN.STA)
wlan.connect(config.WIFI_SSID, auth=(None, config.WIFI_PASS), timeout=50000)
#wlan.connect(ssid='F107', auth=(WLAN.WPA2, 'Champlain@2022'))
while not wlan.isconnected():
	pass
	#time.sleep(2)
    #machine.idle()
print('\n')
print("WiFi connected succesfully to: ")
print(wlan.ifconfig()) # Print IP configuration
#pycom.rgbled(0xFFFF00) # Yellow
time.sleep(5)


# user specified callback function
def customCallback(client, userdata, message):
	print("Received a new message: ")
	print(message.payload)
	print("from topic: ")
	print(message.topic)
	print("--------------\n\n")

# configure the MQTT client
pycomAwsMQTTClient = AWSIoTMQTTClient(config.CLIENT_ID)
pycomAwsMQTTClient.configureEndpoint(config.AWS_HOST, config.AWS_PORT)
pycomAwsMQTTClient.configureCredentials(config.AWS_ROOT_CA, config.AWS_PRIVATE_KEY, config.AWS_CLIENT_CERT)

pycomAwsMQTTClient.configureOfflinePublishQueueing(config.OFFLINE_QUEUE_SIZE)
pycomAwsMQTTClient.configureDrainingFrequency(config.DRAINING_FREQ)
pycomAwsMQTTClient.configureConnectDisconnectTimeout(config.CONN_DISCONN_TIMEOUT)
pycomAwsMQTTClient.configureMQTTOperationTimeout(config.MQTT_OPER_TIMEOUT)
pycomAwsMQTTClient.configureLastWill(config.LAST_WILL_TOPIC, config.LAST_WILL_MSG, 1)

pycomAwsMQTTClient.DEBUG = True
##pycomAwsMQTTClient.set_callback(sub_cb)
#pycomAwsMQTTClient.settimeout = settimeout
pycomAwsMQTTClient.connect()

#Connect to MQTT Host
if pycomAwsMQTTClient.connect():
    print('AWS connection succeeded')
elif (not pycomAwsMQTTClient.connect()):
	print('AWS is not connected')

# Subscribe to topic
pycomAwsMQTTClient.subscribe(config.TOPIC, 1, customCallback)
time.sleep(2)

# Send message to host
loopCount = 0
while loopCount < 8:
	pycomAwsMQTTClient.publish(config.TOPIC, "New Message " + str(loopCount), 1)
	loopCount += 1
	time.sleep(5.0)
# while True:    
#     #JSONPayload = '{"state":{"desired":{"property":' + str(loopCount) + '}}}'
#     #deviceShadowHandler.shadowUpdate(JSONPayload, customShadowCallback_Update, 5)
#     #print('\nvoltage: {}, lumen: {}, lux: {}'.format(voltage, light, lux))
#     print("Sending Voltage: ", 'voltage')
#     print("Sending lumen: ", 'LIGHTMess')
#     print("Sending Lux: ", 'LUXMess')
#     #pycom.rgbled(0x00FF00) # Green
#     pycomAwsMQTTClient.publish(config.TOPIC, str('voltage'), 1)
#     pycomAwsMQTTClient.publish(config.TOPIC, str('LIGHTMess'), 1)
#     pycomAwsMQTTClient.publish(config.TOPIC, str('LUXMess'), 1)
#     time.sleep(5)