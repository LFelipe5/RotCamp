from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from redis_om import get_redis_connection, HashModel
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

redis = get_redis_connection(
    host="redis",
    port=6379,
    password="senharedis",
    decode_responses=True
)

class Delivery(HashModel):
    budget: int = 0
    notes: str = ""

    class Meta:
        database = redis

class Event(HashModel):
    delivery_id: str = ""
    type: str
    data: str

    class Meta:
        database = redis

@app.post('/deliveries/create')
async def create(request: Request):
    body = await request.json()
    delivery = Delivery(budget=body['data']['budget'], notes=body['data']['notes'])
    return delivery