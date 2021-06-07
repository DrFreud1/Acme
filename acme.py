"""
The following variables of ranges will be used to calculate the time 
of the day in which the work was carried out, and to calculate paymentes accordingly
This program interpretes 00:00 as 24:00, as no external libraries are allowed and 
the usage of datetime library is not allowed
"""

morning_range = range(0,9)
afternoon_range = range(9,19)
night_range = range(18,25)

"""
The function clean_input is used to format the user's input, so it can be understood by the program
"""

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

"""
IsWeekend function determines if some part of the input corresponds
to a day of the weekend to calculate payments accordingly
"""

def IsWeekend(day):
    flag = True
    current_day = day[0:2]
    if current_day == 'MO' or current_day == 'TU' or current_day == 'WE' or current_day == 'TH' or current_day == 'FR':
        flag = False
    return flag
        
"""
calculate_payment function calculates the payments of the employees accoring to the hours
they have worked
"""
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
        elif not IsWeekend(tuple[0]):
            if tuple[1] in morning_range and tuple[2] in morning_range:
                payment += (tuple[2] - tuple[1]) * 25
            elif tuple[1] in afternoon_range and tuple[2] in afternoon_range:
                payment += (tuple[2] - tuple[1]) * 15
            elif tuple[1] in night_range and tuple[2] in night_range:
                payment += (tuple[2] - tuple[1]) * 20
    return payment

if __name__ == '__main__':

    with open("inputs.txt") as f:
        txt = f.read().splitlines() 
        for input in txt: 
            employee_name, working_hours = clean_input(input)
            payment = calculate_payment(working_hours)
            
            print("The amount to pay {} is: {}".format(employee_name,payment))
    