from keep_alive import keep_alive
import time
from temp import weather
import json
import datetime

# Run continuously
keep_alive()

while(True):
    ottawa = weather('Ottawa')
    waterloo = weather('Waterloo')
    diff = ottawa-waterloo
    now = datetime.datetime.now()
    with open('./templates/public/data.json', 'r+') as f:
        data = json.load(f)
        print(len(data))
        if(len(data)>59):
            del data[list(data.keys())[0]]
        data[now.strftime("%d-%m-%Y %H:%M:%S")] = diff
        f.seek(0)
        json.dump(data, f, indent=4)
        f.truncate()
    time.sleep(60)
