import time
import paho.mqtt.client as mqtt_client
import random
import requests
from loguru_settings import logger


broker="broker.emqx.io"

try:
    unique_id = '123131'
    logger.info("Уникальный id выдан успешно")
except requests.exceptions.ConnectionError:
    logger.error("Сервер не запущен")

client = mqtt_client.Client(
   mqtt_client.CallbackAPIVersion.VERSION1, 
   unique_id
)

print("Connecting to broker",broker)
print(client.connect(broker))
client.loop_start() 
print("Publishing")

for i in range(3):
    state = f"Зачем ты это принимаешь? Ну на тогда рандомное число: {random.randint(0, 100)}"
    client.publish("lab/leds/state", state)
    logger.info("Успешно отправлено сообщение - " + state)
    time.sleep(2)
    
logger.warning("Publisher перестал работать")  
client.disconnect()
client.loop_stop()