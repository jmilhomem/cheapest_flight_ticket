# BEXS Challenge - Cheapest Flight Ticket
This repo contains the script developed to list the cheapest flight ticket considering a list of tickets.

![alt text](https://image.freepik.com/free-vector/airplane-line-path-go-travel-route-airplane-flight-route-with-start-point-dash-line-vector_48946-60.jpg "")

## Business Context
1. It is desired that the application considers the possible routes and its values to suggest the best route, considering the cheapest flight ticket price.
2. Each route has a price, which should be considered inside a file as the following example.

## Input Example ##
```csv
GRU,BRC,10
BRC,SCL,5
GRU,CDG,75
GRU,SCL,20
GRU,ORL,56
ORL,CDG,5
SCL,ORL,20
```

## Business Requirements

1. One file will be informed during the execution calling via shell.
2. A prompt needs to show up requesting the origin-destination.
3. Considering the source-destination information, the program must return the cheapest Flight Ticket, regardless the route.

## How to Install?
1. Dependencies:  
	1. Python 3.6  
	2. Execution of the make file
	3. File created and updated in the __"files" folder__

2. OS X & Linux:  
	1. To install the enviroment, run: ```make ```

## How to run the program?

Firt, start your python virtualenv running the command ```source .env/bin/activate```

* Run: ```make run input-file.txt``` to start the main process.
* Inform the origin-destination: ```GRU-CDG```


## Testing

TBD
