def add_time(start, duration, weekday = False):
    
    calendar = ['null', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'] 
    
    if weekday is not False :
        datepos = calendar.index(weekday.title())
    elif weekday is False :
        datepos = 0
    
    
    newday = 0    
    AMPM = start.split(" ")[1]
    starthour = start[:start.find(':')]
    startmin = start[start.find(':') + 1:start.find(':') + 3]
        
    addhour = duration[:duration.find(':')]
    addmin = duration[duration.find(':') + 1:duration.find(':') + 3]
    
    if AMPM == 'PM' :
        if starthour != '12' :
            starthour = int(starthour) + 12
    elif AMPM == 'AM' :
        if starthour != '12' :
            starthour = '0' + starthour
        elif starthour == '12' :
            starthour = starthour

    newhour = int(starthour) + int(addhour)
    newmin = int(startmin) + int(addmin)
    
    while newmin > 59 :
        newmin = newmin - 60
        newhour = newhour + 1
    
    while newhour >= 24 :
        newhour = newhour - 24
        if newday == 0 :
            newday = 1
        elif newday is not None :
            newday = newday + 1

    
    datepos = int(datepos) + int(newday)
    
    while datepos > 7 :
        datepos = datepos - 7
    
    
            
    if newhour < 12 :
        newhour = newhour
        newampm = 'AM'
    elif newhour >= 12 :
        newhour = newhour - 12
        newampm = 'PM'

    if newhour == 0 :
        newhour = 12
    
    
    if newday < 1 and weekday is False :
        
        if newmin < 10 :
            returntime = f"{newhour}:0{newmin} {newampm}"
        elif newmin >= 10 :
            returntime = f"{newhour}:{newmin} {newampm}"
    if newday < 1 and weekday is not False :
        if newmin < 10 :
            returntime = f"{newhour}:0{newmin} {newampm}, {calendar[datepos]}"
        elif newmin >= 10 :
            returntime = f"{newhour}:{newmin} {newampm}, {calendar[datepos]}"
    
    if newday == 1 and weekday is False :
        if newmin < 10 :
            returntime = f"{newhour}:0{newmin} {newampm} (next day)"
        elif newmin >= 10 :
            returntime = f"{newhour}:{newmin} {newampm} (next day)"
    if newday == 1 and weekday is not False :
        if newmin < 10 :
            returntime = f"{newhour}:0{newmin} {newampm}, {calendar[datepos]} (next day)"
        elif newmin >= 10 :
            returntime = f"{newhour}:{newmin} {newampm}, {calendar[datepos]} (next day)"
    
    
    
    if int(newday) > 1 and weekday is False:
        if newmin < 10 : 
            returntime = f"{newhour}:0{newmin} {newampm} ({newday} days later)"
        elif newmin >= 10 :
            returntime = f"{newhour}:{newmin} {newampm} ({newday} days later)"
    if int(newday) > 1 and weekday is not False:
        if newmin < 10 : 
            returntime = f"{newhour}:0{newmin} {newampm}, {calendar[datepos]} ({newday} days later)"
        elif newmin >= 10 :
            returntime = f"{newhour}:{newmin} {newampm}, {calendar[datepos]} ({newday} days later)"    

    
    
    return returntime
    
#add_time("3:00 PM", "3:10")
# Returns: 6:10 PM

#add_time("11:30 AM", "2:32", "Monday")
# Returns: 2:02 PM, Monday

#add_time("11:43 AM", "00:20")
# Returns: 12:03 PM

#add_time("10:10 PM", "3:30")
# Returns: 1:40 AM (next day)

#add_time("11:43 PM", "24:20", "tueSday")
# Returns: 12:03 AM, Thursday (2 days later)

#add_time("6:30 PM", "205:12")
# Returns: 7:42 AM (9 days later)    