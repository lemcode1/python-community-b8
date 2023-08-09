# stations
# trains
# time
stations = ['hyderabad','guntur','narasaraopet','piduguralla','vijayawada','ongole','nellore','tirupati','kakinada','vizag']
trains = [
	{
	  "name":"Venkatadri express",
	  "train_no": 1234,
	  "train_type": "Express",
	  "stations" : ['hyderabad','guntur','vijayawada','ongole','nellore','tirupati','kakinada','vizag'],
	  "time": "16:50"
	},
	{
	  "name":"Kachiguda Passenger",
	  "train_no": 543222,
	  "train_type": "Passenger",
	  "stations" : ['hyderabad','guntur','narasaraopet','piduguralla','vijayawada','ongole','nellore','tirupati','kakinada','vizag'],
	  "time": "07:50"
	},
	{
	  "name":"Gauthami SuperFast",
	  "train_no": 543222,
	  "train_type": "SuperFast",
	  "stations" : ['hyderabad','guntur','vijayawada','tirupati','kakinada','vizag'],
	  "time": "07:50"
	},
	{
	  "name":"Vande Bharat",
	  "train_no": 543222,
	  "train_type": "SuperFast",
	  "stations" : ['hyderabad','guntur','vijayawada','rajamundry','vizag'],
	  "time": "07:10"
	}
]

def find_trains_by_destination(destination_name):
	if destination_name in stations:
		final_trains = []
		for train in trains:
			if destination_name in train.get('stations'):
				final_trains.append(train)
		return final_trains
	else:
		print("This station is not available")


destination_station = input("Please enter destination to find trains:")

trains_availale = find_trains_by_destination(destination_station)
# print(trains_availale)s
if trains_availale is not None:
	for train in trains_availale:
		print(train.get('train_no'))
		print(train.get('time'))
		print(train.get('name'))
		print()
