#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import time
import csv,json


# Function to convert a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath):
     
    jsonArray = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            jsonArray.append(row)
    return jsonArray
    #return json.dumps(jsonArray, indent=4)


async def client():
    uri = "ws://localhost:9001"
    async with websockets.connect(uri) as websocket:
        json_data = '{"data_type":"position","x":"3","y":"6"}'

        # data = make_json('csv_file.csv')
        # json_data = {"data_type":"map_path","data":data}
        # json_data = json.dumps(json_data, indent=4)

        #json_data.append(data)
        #print(json_data)

        await websocket.send(json_data)
        print("Data Sent")
        #print(f"> {data}")

        # greeting = await websocket.recv()
        # print(f"< {greeting}")




#def qucick_run():
asyncio.get_event_loop().run_until_complete(client())
#asyncio.get_event_loop().run_forever(client())

#for x in range(100):
#    qucick_run()
#    time.sleep(1)



    
