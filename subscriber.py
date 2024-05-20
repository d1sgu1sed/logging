from datetime import datetime, timedelta
import time
import paho.mqtt.client as mqtt_client
import requests
import random
from loguru_settings import logger


client_ids = {}

WARNING_THRESHOLD = 60 * 3

last_message_time = None

broker = "broker.emqx.io"


# def check_unique_id(unique_id):
#     if unique_id in client_ids:
#         return False
#     else:
#         client_ids[unique_id] = datetime.now()
#         return True
    

def on_message(client, userdata, message):
    global last_message_time
    last_message_time = datetime.now()
    sender_id = message.mid 
    # if not check_unique_id(sender_id):
    #     logger.error("Попытка посылки данных двумя разными клиентами с одним ID")
    # logger.debug(f'ID отправителя - {sender_id}')
    time.sleep(1)
    data = str(message.payload.decode("utf-8"))
    logger.debug("Успешно принято сообщение - " + data)


try:
    unique_id = requests.get('http://127.0.0.1:8000/get_id').json()[0]
    logger.info("Уникальный id выдан успешно")
except requests.exceptions.ConnectionError:
    logger.error("Сервер не запущен")


client = mqtt_client.Client(
   mqtt_client.CallbackAPIVersion.VERSION1, 
   unique_id
)
client.on_message=on_message

print("Connecting to broker",broker)
client.connect(broker) 
client.loop_start() 
print("Subcribing")
logger.info("Подписка прошла успешно")
client.subscribe("lab/leds/state")
try:
    while True:
        if last_message_time is not None and (datetime.now() - last_message_time) > timedelta(seconds=WARNING_THRESHOLD):
            logger.warning("От publisher давно нет сообщений")
        time.sleep(60)
except KeyboardInterrupt:
    client.disconnect()
    logger.info("Остановление подписки")
    client.loop_stop()