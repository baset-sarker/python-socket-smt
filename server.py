from websocket_server import WebsocketServer
import time,random
import threading

import json 

# send the path data to the client 
# modify this function
def send_path_data_to_client(client):
	path_locations = [(3,4),(4,5)] # get it from your generated code
	json_data = {"data_type":"path_data","data":path_locations}
		

# Called for every client connecting (after handshake)
def new_client(client, server):
	print("New client connected and was given id %d" % client['id'])
	server.send_message_to_all("Hey all, a new client has joined us")


# Called for every client disconnecting
def client_left(client, server):
	print("Client(%d) disconnected" % client['id'])


# Called when a client sends a message
def message_received(client, server, message):
	'''{"data_type":"start","start_point":{"x":"3","y":"6"},"end_point":{"x":"5","y":"6"}}'''

	print("Received Data")
	print(message)

	try:
		message_data = json.loads(message)
		if message_data['data_type'] == "start":
			start_x = message_data['start_point']['x']
			start_y = message_data['start_point']['y']
			end_x = message_data['end_point']['x']
			end_y = message_data['end_point']['y']

			th = threading.Thread(target=send_path_data_to_client(client))
			th.start()
			
		if message_data['data_type'] == "stop":
			print("stop")
			
		if message_data['data_type'] == "position":
			print("position data:"+str(message_data['x'])+','+str(message_data['x']))
			server.send_message_to_all(json.dumps(message_data))
		
		if message_data['data_type'] == "path_data":
			print("position data:"+str(message_data["data"]))
			server.send_message_to_all(json.dumps(message_data))

		

	except ValueError as e:
		print("json parse error")
		return False

PORT=9001
#SERVER = '192.168.0.163'
SERVER ="localhost"
server = WebsocketServer(PORT,SERVER)
server.set_fn_new_client(new_client)
server.set_fn_client_left(client_left)
server.set_fn_message_received(message_received)
server.run_forever()





