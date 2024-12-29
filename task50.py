def convert_time(time_str):
    if 'AM' in time_str or 'PM' in time_str:
        time, period = time_str[:-2].strip(), time_str[-2:]
        hours, minutes = map(int, time.split(':'))
        
        if period == 'AM':
            if hours == 12:
                hours = 0 
        else: 
            if hours != 12:
                hours += 12  
        
        return f"{hours:02}:{minutes:02}" 
    else:
    
        hours, minutes = map(int, time_str.split(':'))
        period = 'AM'
        
        if hours >= 12:
            period = 'PM'
            if hours > 12:
                hours -= 12 
        else:
            if hours == 0:
                hours = 12  
        
        return f"{hours}:{minutes:02} {period}"

print(convert_time("02:30 PM"))  
print(convert_time("14:30"))     
print(convert_time("12:00 AM"))   
print(convert_time("12:00 PM"))  
print(convert_time("00:15"))  