'''
this function creates a calendar page 
for the specified year and month
'''
def create_calendar_page(month=None, year=None):
    import datetime
    dt=datetime.datetime.today()
    
    if month==None:
        month=dt.month
    if year==None:
        year=dt.year
    dt_1=datetime.datetime(year, month, 1)
   
    numbers='01 02 03 04 05 06 07 08 09 10 \
11 12 13 14 15 16 17 18 19 20 \
21 22 23 24 25 26 27 28'

    menu='1 --------------------\n\
2 MO TU WE TH FR SA SU\n\
3 --------------------\n'
    itogo=' '*((dt_1.weekday())*3)+numbers

    otvet=menu + "4 "+ itogo[:21]+'\n'+"5 "+itogo[21:42]+'\n'\
    +'6 '+itogo[42:63]+'\n'+'7 '+itogo[63:84]+'\n'\
    +'8 '+itogo[84:] 

    return otvet

print (create_calendar_page(1,2022))