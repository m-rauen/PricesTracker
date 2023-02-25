def format_date(going, returning):
    months = {
        1:'jan.', 
        2:'fev.', 
        3:'mar.', 
        4:'abr.', 
        5:'mai.', 
        6:'jun.', 
        7:'jul.', 
        8:'ago.', 
        9:'set.', 
        10:'out.', 
        11:'nov.', 
        12:'dez.'
    }
    
    going_day = int(going[0])
    gmonth = int(going[1])
    going_month = months.get(gmonth)
    going_year = int(going[2])
    going_dt = '{} de {} de {}'.format(going_day,going_month,going_year)
    
    returning_day = int(returning[0])
    rmonth = int(returning[1])
    returning_month = months.get(rmonth)
    returning_year = int(returning[2])
    returning_dt = '{} de {} de {}'.format(returning_day,returning_month, returning_year)
    
    del gmonth, rmonth 
    return going_dt, returning_dt
    

def inp_receiver():
    #TODO: change CLI to GUI;
    #TODO: receive input via mini popup window
    
      print("""
          --------------------------------
          Welcome to FlightPrices-Tracker
          --------------------------------
          """)
      
      origin = input(str('Departure: ')).strip().capitalize()
      departure = input(str('Arrival: ')).strip().capitalize()
      
      gng_date = input((str('Going date (DD/MM/YYYY): '))).split('/')
      rturning_date = input(str('Returning date (DD/MM/YYYY): ')).split('/')
      
      going_date, returning_date = format_date(gng_date, rturning_date)
      
      return origin, departure, going_date, returning_date
