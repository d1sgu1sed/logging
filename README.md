# Инструкция для просмотра логов
## ВАЖНО! В файле логи выглядят немного иначе чем в консоли
1. Для просмотра Error сначала запустите subscriber.py или publisher.py
```
python subscriber.py 
2024-05-21 at 00:26:13 | ERROR | subscriber.py:42 | Сервер не запущен | big-ivan
```
2.  Для просмотра Info достаточно запустить FastAPI сервер
```
uvicorn user_service:app
2024-05-21 at 00:28:32 | INFO | user_service.py:9 | Успешно запщуен сервер | big-ivan
```
3. Для просмотра Warning надо запустить сервер, запустить subscriber.py и publisher.py, после чего подождать 5 минут, тогда выведется предупреждение, что давно не было публикаций
```
uvicorn user_service:app
python subscriber.py
python publisher.py
2024-05-21 at 00:13:00 | WARNING | subscriber.py:58 | От publisher давно нет сообщений | big-ivan
```
4. Для Debug достаточно запустить subscriber.py и publisher.py, в лог выведутся получаемое и отправляемое сообщения
```
uvicorn user_service:app
python subscriber.py
python publisher.py
2024-05-21 at 00:09:36 | DEBUG | subscriber.py:31 | Успешно принято сообщение - Зачем ты это принимаешь? Ну на тогда рандомное число: 77 | big-ivan
2024-05-21 at 00:09:37 | INFO | publisher.py:29 | Успешно отправлено сообщение - Зачем ты это принимаешь? Ну на тогда рандомное число: 65 | big-ivan
```
