car_started = False
while True:
    userInput = input(">").lower()
    if userInput == "help":
        print("""
start - to start the car 
stop - to stop the car
quit - to exit 
        """)
    elif userInput == "start":
        if car_started:
            print("Car is already Started")
        else:
            car_started = True
            print("Car started... Ready to go!")
    elif userInput == "stop":
        if not car_started:
            print("Car is already stopped")
        else:
            car_started = False
            print("Car stopped.")
    elif userInput == "quit":
        break
    else:
        print("I don't understand that...")
