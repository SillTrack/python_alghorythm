import hashlib
from uuid import uuid4


salt = uuid4().hex
cache_object = {}


def check_page(url):
    if cache_object.get(url):
        print(f'Данный адрес: {url} присутствует в кеше')
    else:
        temp = hashlib.sha256(salt.encode() + url.encode()).hexdigest()
        cache_object[url] = temp    
        print(cache_object)



check_page('https://gb.ru/lessons/141728')
check_page('https://gb.ru/lessons/1417289')
check_page('https://gb.ru/lessons/14172890')
check_page('https://gb.ru/lessons/141728')