import datetime

while True:
    city = input("Enter city: ")

    current_time = datetime.datetime.now()
    hour = current_time.hour - 3

    ## Because of timezone GMT + 3 (Nairobi)

    minute = current_time.minute
    second = current_time.second

    if city == "Boston":
        hour = hour - 4

    elif city == "Tokyo":
        hour = hour + 9

    elif city == "Chicago":
        hour = hour - 5

    elif city == "Nairobi":
        hour = hour + 3

    elif city == "Seattle":
        hour = hour - 7

    if city == "Cairo":
        hour = hour - 2

    elif city == "Karachi":
        hour = hour + 5

    elif city == " Shanghai":
        hour = hour + 8

    elif city == "Dallas":
        hour = hour -6

    elif city == "Islamabad":
        hour = hour + 5

    elif city == " Kolkata":
        hour = hour + 5
        minute = minute + 30

    elif city == "exit":

        break

    else:
        print(city, "is not added")
        city = "GMT"

    #Printing the name of the city and it's corresponding time

    print(city, str(hour) + ":" + str(minute) + ":" + str(second))
