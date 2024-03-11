# pip install redis
import redis
from datetime import datetime

# connect to server
r = redis.Redis(host='localhost', port=6379, db=0)

# write dictionary to server using mset
r.mset({"Milk": "Lactose", "Bread": "Gluten"})

# write timestamp to 'nums' list
t = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
r.rpush('nums', t)
