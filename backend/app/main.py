from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from misc.models import Delivery, Event
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['http://localhost:3000'],
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/deliveries/{pk}/state')
async def get_state(pk: str):
    pass

@app.post('/deliveries/create')
async def create(request: Request):
    body = await request.json()
    delivery = Delivery(
        budget=body['data']['budget'],
        notes=body['data']['notes']
    ).save()
    event = Event(
        delivery_id=delivery.pk,
        type=body['type'],
        data=json.dumps(body['data'])
    ).save()
    state = consumers.create_delivery({}, event)
    return event