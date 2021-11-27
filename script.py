from keep_alive import keep_alive
import time
from temp import weather
import json
import datetime

# Start the server
keep_alive()

while(True):
    # Get weather info
    ottawa = weather('Ottawa')     # City 1
    waterloo = weather('Waterloo') # City 2
    
    # Temperature Difference
    diff = ottawa-waterloo

    # Timestamp
    now = datetime.datetime.now()
    
    # Storing data in data.json
    with open('./templates/public/data.json', 'r+') as f:
        # Getting current file info
        data = json.load(f)
        # Checking if the data is more than 1 hour
        if(len(data)>59):
            # Deletes the data in case it is more than 1 hour
            del data[list(data.keys())[0]]
        
        # Adding new data
        data[now.strftime("%d-%m-%Y %H:%M:%S")] = diff
        f.seek(0)
        json.dump(data, f, indent=4)

        # Removing the old data
        f.truncate()
        
    # Wait for 60s before looping
    time.sleep(60)