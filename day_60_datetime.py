import datetime

today = datetime.date.today()
# header
print("datetime event")
print()
while True:
    # event
    event = input("What is your event: ")
    try:
        # user input the date
        eventyear = int(input("Please enter the year: "))
        eventmonth = int(input("Please enter the month: "))
        eventday = int(input("Please enter the day: "))
        # users date as a datetime object
        eventdate = datetime.date(year=eventyear, month=eventmonth, day=eventday)
        days_until_event = eventdate - today
        days = days_until_event.days
        # display the days until
        print(f"There are {days} days until {event}")

        if eventdate > today:
            print(f"{event} coming soon")
        elif eventdate < today:
            print(f"Hope you enjoyed {event}")
        else:
            print(f"It is {event} day")
    except ValueError:
        print("There was an error. Please enter a valid date")

