from datetime import date
    
day = 0
minut = 0
sex = 0

while(True):
    
    def leap_year_detector(year):
        leap_flag = False
        if( (year % 400) == 0 and (year % 4) == 0):
            leap_flag = True
        elif(year % 100 == 0):
            leap_flag = False
        else:
            leap_flag = True
            
        return leap_flag
    
    name = input("Hello please enter your  name : ")
    year = int(input("Now enter your birth year : "))
    
    print("Thank you {} for providing information.".format(name))
    
    # Calculate current year to calculate age
    current_year = int(date.today().year)
    
    leap_result = leap_year_detector(year)
    age = current_year - year
    
    if(leap_result == True):
        day = age * 366
        minut =  day * 24 * 60
        sex = minut * 60
    
    if(leap_result == False):
        day = age * 365
        minut =  day * 24 * 60
        sex = minut * 60
    
    print("We analyzed based on input provided.")
    if(leap_result == True):
        print("{} we are considering leap year rules.".format(name))
    print("{} your age is {}.".format(name, age))
    print("{} your are living {} days, {} minutes and {} seconds.".format(name, day, minut, sex))
    
    message = """
    You want to try again.
    Any - Yes
    0 - No
    """
    conti = input(message)
    
    if(conti == "0"):
        print("Thank You")
        break