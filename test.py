from datetime import datetime
from hashlib import md5
import json

import requests


print(requests.get('http://127.0.0.1:8000/get_id').json()[0])