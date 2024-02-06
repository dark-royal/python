
def seconds_since_midnight(*args):
    for value in args:
        if(hour > 0 | hour <=24 & minute > 0 | minute<= 60 & second > 0 | second <= 60):
             hours_in_seconds =  hour * 60 * 60
             minute_in_second = minute * 60
             time =  hours_in_seconds + minute_in_second + second
    return time

seconds_since_midnight(1,30,45)










