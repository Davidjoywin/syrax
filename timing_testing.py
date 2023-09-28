from datetime import datetime, timedelta

from timing import Present, Past, Future


now = datetime.now

present = Present(now())
print(present)

past = Past(now())
print(present)

future = Future(now())
print(future)

