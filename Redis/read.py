# pip install redis
import redis

# connect to server
r = redis.Redis(host='localhost', port=6379, db=0)

# read values using get method
keys = ["Milk", "Bread"]

for key in keys:
    value = r.get(key)
    print(f"{key}: {value.decode('utf-8') if value else 'Key not found'}")
