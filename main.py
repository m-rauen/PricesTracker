from cli.input import *
import src.scrapper as scrapper

def main():
    org, dept, begin_dt, end_dt = inp_receiver()
    scrapper.expedia_scrapper(org, dept, begin_dt, end_dt)
    scrapper.decolar_scrapper(org, dept, begin_dt, end_dt)
    
if __name__ == '__main__':
    main()
      
    


