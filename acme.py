"""now variable will be used across the code to define the time of the day"""

morning_range = range(0,9)
afternoon_range = range(9,19)
night_range = range(18,24)

def clean_input(user_input):
    clean_input = []
    employee_name, working_days = user_input.split("=")
    split_working_days = working_days.split(",")

    for days in split_working_days:
        day = days[:2]; hour_begin = days[2:4]; hour_end = days[8:10]
        # hour_begin, minute_begin = str_hour_begin.split(":"); hour_end, minute_end = str_hour_end.split(":")
        # hour_begin = time(hour=int(hour_begin), minute=int(minute_begin), second=0); hour_end = time(hour=int(hour_end), minute=int(minute_end), second=0)
        hours_per_day = (day, int(hour_begin), int(hour_end))
        clean_input.append(hours_per_day)
    return employee_name, clean_input

def IsWeekend(day):
    flag = True
    current_day = day[0:2]
    if current_day == 'MO' or current_day == 'TU' or current_day == 'WE' or current_day == 'TH' or current_day == 'FR':
        flag = False
    return flag
        

def calculate_payment(working_hours):
    payment = 0
    for tuple in working_hours:
        if IsWeekend(tuple[0]):
            if tuple[1] in morning_range and tuple[2] in morning_range:
                payment += (tuple[2] - tuple[1]) * 30
            elif tuple[1] in afternoon_range and tuple[2] in afternoon_range:
                payment += (tuple[2] - tuple[1]) * 20
            elif tuple[1] in night_range and tuple[2] in night_range:
                payment += (tuple[2] - tuple[1]) * 25
        elif IsWeekend(tuple[0]) == False:
            if tuple[1] in morning_range and tuple[2] in morning_range:
                payment += (tuple[2] - tuple[1]) * 25
            elif tuple[1] in afternoon_range and tuple[2] in afternoon_range:
                payment += (tuple[2] - tuple[1]) * 15
            elif tuple[1] in night_range and tuple[2] in night_range:
                payment += (tuple[2] - tuple[1]) * 20
        # print(payment)
        # print(tuple[0])
    return payment

if __name__ == '__main__':

    # txt = "RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00"
    txt = "ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00"
    employee_name, working_hours = clean_input(txt)
    
    # print(employee_name, working_hours)
    payment = calculate_payment(working_hours)
    print("The amount to pay {} is: {}".format(employee_name,payment))
    