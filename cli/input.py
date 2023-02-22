import datetime as dt

def inp_receiver():
    print("""
          --------------------------------
          Welcome to FlightPrices-Tracker
          --------------------------------
          """)
    
    origin = input(str('Departure: ')).strip().capitalize()
    departure = input(str('Arrival: ')).strip().capitalize()
    
    going_date = input((str('Going date (DD/MM/YY): '))).split('/')
    day = int(going_date[0])
    month = int(going_date[1])
    year = int(going_date[2])
    del going_date
    going_date = dt.date(year, month, day)
          
    returning_date = input(str('Returning date (DD/MM/YYYY): ')).split('/')
    day = int(returning_date[0])
    month = int(returning_date[1])
    year = int(returning_date[2])
    del returning_date
    returning_date = dt.date(year, month, day)
    
    return origin, departure, going_date, returning_date
