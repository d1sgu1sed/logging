from fastapi import FastAPI
from hashlib import md5
from datetime import datetime
from loguru_settings import logger


app = FastAPI()

logger.info("Успешно запщуен сервер")

@app.get('/get_id')
async def get_id():
    logger.info("Вызван метод get_id()")
    return{md5(str(datetime.now()).encode('utf-8')).hexdigest()}