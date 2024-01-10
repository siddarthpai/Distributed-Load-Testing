## Distributed Load Testing System

**Team 39:**

Siddarth.D.Pai - PES2UG21CS925

C Ujwal - PES2UG21CS131

Charan S Gowda - PES2UG21CS140

Thaksha Ganesh - PES2UG21CS575

## Goal

Design and build a distributed load-testing system that co-ordinates between  
multiple driver nodes to run a highly concurrent, high-throughput load test on a  
web server. This system will use Kafka as a communication service.

![The Architecture Diagram of the entire Distributed Load Testing system](https://i.imgur.com/dEAZWyX.png)

## How to run our code?

1. Start kafka using `sudo systemctl start kafka`
2. Run our server using `go run main.go`
3. Run our intermediate Kafka Node using `python3 kafka_intermediate.py`
4. Now we can run our driver node on terminal using `python3 driver.py`

- Note : We can run multiple driver nodes by running this code on multiple terminal instances which will act as individual processes.

1. We can now run our Orchestrator node using `python3 orch.py`
2. You will now be presented with 4 options:

   1.Avalanche Testing

   2.Tsunami Testing

   3.Node Data

   4.Exit

3. User can now make respective input choices to proceed.

4. User can also go to endpoints on the server

   `/metrics -> which will show the total number of requests and responses made to the server`

   `/ping -> returns a "pong" message to show server is active`
