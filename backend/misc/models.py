from redis_om import HashModel, get_redis_connection

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