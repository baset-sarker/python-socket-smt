#!/usr/bin/env python

# WS client example

import asyncio
import websockets
import time
import csv,json


#uri = "ws://localhost:9001"
uri = "ws://192.168.0.163:9001"

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


async def send_live_location(x,y):

    async with websockets.connect(uri) as websocket:
        json_data = {"data_type":"position","x":x,"y":y}
        json_data = json.dumps(json_data, indent=4)
        await websocket.send(json_data)
        print("Data Sent"+json_data)
        #print(f"> {json_data}")

        # greeting = await websocket.recv()
        # print(f"< {greeting}")

async def send_data_from_csv(csv_path):
    async with websockets.connect(uri) as websocket:
        #json_data = '{"data_type":"position","x":,"y":"6"}'

        data = make_json(csv_path)
        json_data = {"data_type":"map_path","data":data}
        json_data = json.dumps(json_data, indent=4)

        await websocket.send(json_data)
        print("CSV Data Sent")
        #print(f"> {data}")

        # greeting = await websocket.recv()
        # print(f"< {greeting}")

x=3
y=4
asyncio.get_event_loop().run_until_complete(send_live_location(x,y))

#asyncio.get_event_loop().run_until_complete(send_data_from_csv('csv_file.csv'))




    
