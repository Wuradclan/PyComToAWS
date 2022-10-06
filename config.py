
# wifi configuration
WIFI_SSID = 'CIK1000M_AC-ebc0'
WIFI_PASS = '3c9066cfebc0'

# AWS general configuration
AWS_PORT = 8883
AWS_HOST = 'am771eam97wll-ats.iot.us-east-1.amazonaws.com'
AWS_ROOT_CA = '/flash/cert/AmazonRootCA1.pem' #'/flash/cert/aws_root.ca'
AWS_CLIENT_CERT = '/flash/cert/certificate.pem.crt'#'/flash/cert/aws_client.cert'
AWS_PRIVATE_KEY = '/flash/cert/private.pem.key'

################## Subscribe / Publish client #################
CLIENT_ID = 'PycomPublishClient'
TOPIC = 'PublishTopic'
OFFLINE_QUEUE_SIZE = -1
DRAINING_FREQ = 2
CONN_DISCONN_TIMEOUT = 10
MQTT_OPER_TIMEOUT = 5
LAST_WILL_TOPIC = 'PublishTopic'
LAST_WILL_MSG = 'To All: Last will message'

####################### Shadow updater ########################
# THING_NAME = "Morad_PyCOM" #"my thing name"
# CLIENT_ID = "ShadowUpdater"
# CONN_DISCONN_TIMEOUT = 10
# MQTT_OPER_TIMEOUT = 5

# ####################### Delta Listener ########################
# THING_NAME = "Morad_PyCOM"#"my thing name"
# CLIENT_ID = "DeltaListener"
# CONN_DISCONN_TIMEOUT = 10
# MQTT_OPER_TIMEOUT = 5

# ####################### Shadow Echo ########################
# THING_NAME = "Morad_PyCOM"#"my thing name"
# CLIENT_ID = "ShadowEcho"
# CONN_DISCONN_TIMEOUT = 10
# MQTT_OPER_TIMEOUT = 5


# arn:aws:iot:us-east-1:059831388641:thing/MoradPycom2
