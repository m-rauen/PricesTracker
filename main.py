from cli.input import *
from src.scrapper import expedia_scrapper, decolar_scrapper

def main():
    org, dept, begin_dt, end_dt = inp_receiver()
    expedia_scrapper(org, dept, begin_dt, end_dt)
    decolar_scrapper(org, dept, begin_dt, end_dt)

if __name__ == '__main__':
    main()


      
    


