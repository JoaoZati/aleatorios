from datetime import timedelta, datetime
import time

timed = timedelta()

now = datetime.now()
time.sleep(2)
after = datetime.now()

diff = after - now
timed += diff
