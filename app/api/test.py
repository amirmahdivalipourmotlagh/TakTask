import requests as rq


res = rq.get('http://localhost:8000/api/')
dicter = list(res.text)
print(dicter)
print(type(dicter))