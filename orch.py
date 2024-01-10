from kafka import KafkaConsumer, KafkaProducer
import time
import threading
import json
from datetime import datetime, timedelta
import os

def clear_terminal():
    if os.name == 'posix':  
        os.system('clear')
    elif os.name == 'nt':   
        os.system('cls')
    else:
        None


drivers = {}


if __name__ == "__main__":
    producer = KafkaProducer(value_serializer = lambda message:json.dumps(message).encode('utf8'))
    producer.send(topic="status",value=drivers)
    producer.flush()
    consumer4 = KafkaConsumer(value_deserializer = lambda message: json.loads(message.decode('utf8')))
    consumer4.subscribe(['status'])
    while True:
        msg = consumer4.poll(200)
        if len(msg) > 0 : 
            msg = msg[next(iter(msg))][0].value
            drivers = msg
            break
    
    while True:
        print("-"*10)
        print()
        print("Enter the type of test: ")
        print()
        print("1. Avalanche Testing")
        print("2. Tsunami Testing")
        print("3. Available Drivers")
        print("4. Exit")
        print()
        print("-"*10)
        print()
        value = int(input("Enter your choice: "))
        clear_terminal()
        
        if value==1:
            print()
            value = int(input("Enter the number of message count per driver: "))
            print()
            clear_terminal()
            test_id = datetime.now().strftime("%Y%m%d%H%M%S")
            test_config = test_config = {
                    "test_id": test_id,
                    "test_type": "AVALANCHE",
                    "test_message_delay": 0,
                    "message_count_per_driver": value
                }
                
            producer = KafkaProducer(value_serializer = lambda message:json.dumps(message).encode('utf8'))
            producer.send(topic="kafka_test_config",value=test_config)
            producer.flush()
            
            print("-"*10)
            print()
            print("Do you want to proceed with Testing? ")
            print()
            print("1. Yes")
            print("2. No")
            print()
            print("-"*10)
            print()
            value = int(input("Enter your response: "))
            clear_terminal()
            
            if value == 1:  
                print("-"*10)
                print()
                print("Test Running!")
                print()
                print("-"*10)
                trigger = {
                "test_id": test_id,
                "trigger": "YES"
                }
                time.sleep(1.5)

                producer = KafkaProducer(value_serializer = lambda message:json.dumps(message).encode('utf8'))
                producer.send(topic='kafka_trigger', value=trigger)
                producer.flush()
                
                consumer = KafkaConsumer(value_deserializer = lambda message: json.loads(message.decode('utf8')))
                consumer.subscribe(["kafka_metrics"])
                tim=0
                count = 0
                flag=0
                while True:
                    msg = consumer.poll(200)
                    if len(msg) > 0 : 
                        
                        msg = msg[next(iter(msg))][0].value
                        print(json.dumps(msg, indent=4))
                        count+=1
                        if count==1:
                            tim=time.time()
                            flag=1
                            
                    if flag==0:
                        tim=time.time()
                    if count==len(drivers) or (time.time()-tim)>=7:
                        break
                print()
                input("Press Enter")
                clear_terminal()
                
            
            else:
                continue
        
        elif value==2:
            print()
            value = int(input("Enter the number of message count per driver: "))
            delay = int(input("Enter the delay: "))
            print()
            clear_terminal()
            test_id = datetime.now().strftime("%Y%m%d%H%M%S")
            test_config = {
                    "test_id": test_id,
                    "test_type": "TSUNAMI",
                    "test_message_delay": delay,
                    "message_count_per_driver": value
                }
                
            producer = KafkaProducer(value_serializer = lambda message:json.dumps(message).encode('utf8'))
            producer.send(topic="kafka_test_config",value=test_config)
            producer.flush()
            
            print("-"*10)
            print()
            print("Do you want to proceed with Testing? ")
            print()
            print("1. Yes")
            print("2. No")
            print()
            print("-"*10)
            print()
            value = int(input("Enter your response: "))
            clear_terminal()
            if value == 1:  
                print("-"*10)
                print()
                print("Test Running!")
                print()
                print("-"*10)
                trigger = {
                "test_id": test_id,
                "trigger": "YES"
                }
                time.sleep(1.5)

                producer = KafkaProducer(value_serializer = lambda message:json.dumps(message).encode('utf8'))
                producer.send(topic='kafka_trigger', value=trigger)
                producer.flush()
                
                consumer = KafkaConsumer(value_deserializer = lambda message: json.loads(message.decode('utf8')))
                consumer.subscribe(["kafka_metrics"])
                count = 0
                tim=0
                flag=0
                while True:
                    msg = consumer.poll(200)
                    if len(msg) > 0 : 
                        msg = msg[next(iter(msg))][0].value
                        print(json.dumps(msg, indent=4))
                        count+=1
                        if count==1:
                            tim=time.time()
                            flag=1
                    if flag==0:
                        tim=time.time()
                    if count==len(drivers) or (time.time()-tim)>=7:
                        break
                print()
                input("Press Enter")
                clear_terminal()
                
            
            else:
                continue
        
        elif value==3:
            print()
            print("Number of driver:", len(drivers))
            print()
            print(json.dumps(drivers, indent=4))
            print()
            input("Press Enter")
            clear_terminal()
        
        else:
            break
        
