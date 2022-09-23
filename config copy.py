
# wifi configuration
WIFI_SSID = 'WuRAD'
WIFI_PASS = '11111111'

# AWS general configuration
AWS_PORT = 8883
AWS_HOST = 'am771eam97wll-ats.iot.us-east-1.amazonaws.com'
AWS_ROOT_CA = '/flash/cert/AmazonRootCA3.pem' #'/flash/cert/aws_root.ca'
AWS_CLIENT_CERT = '/flash/cert/191a5cf3913fbbfe605be0888b1e6fd62367c7d0e5a2450a68fade499e356191-certificate.pem.crt'#'/flash/cert/aws_client.cert'
AWS_PRIVATE_KEY = '/flash/cert/191a5cf3913fbbfe605be0888b1e6fd62367c7d0e5a2450a68fade499e356191-private.pem.key'

################## Subscribe / Publish client #################
#CLIENT_ID = 'PycomPublishClient'
#TOPIC = 'PublishTopic'
#OFFLINE_QUEUE_SIZE = -1
#DRAINING_FREQ = 2
#CONN_DISCONN_TIMEOUT = 10
#MQTT_OPER_TIMEOUT = 5
#LAST_WILL_TOPIC = 'PublishTopic'
#LAST_WILL_MSG = 'To All: Last will message'

####################### Shadow updater ########################
#THING_NAME = "my thing name"
#CLIENT_ID = "ShadowUpdater"
#CONN_DISCONN_TIMEOUT = 10
#MQTT_OPER_TIMEOUT = 5

####################### Delta Listener ########################
#THING_NAME = "my thing name"
#CLIENT_ID = "DeltaListener"
#CONN_DISCONN_TIMEOUT = 10
#MQTT_OPER_TIMEOUT = 5

####################### Shadow Echo ########################
THING_NAME = "my thing name"
CLIENT_ID = "ShadowEcho"
CONN_DISCONN_TIMEOUT = 10
MQTT_OPER_TIMEOUT = 5
