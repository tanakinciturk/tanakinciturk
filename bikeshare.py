import os
import numpy as np
import re
import datetime


def get_city():
    city = input('Would you like to see data for Chicago, New York, or Washington?\n')

    if city == 'Chicago' or city == 'chicago':
        with open('chicago.csv', 'r') as f:
            data = f.read()
            cityinitial="c"
    elif city == 'New York' or city == 'new york':
        with open('new_york_city.csv', 'r') as f:
            data = f.read()
            cityinitial="n"
    elif city == 'Washington' or city == 'washington':
        with open('washington.csv', 'r') as f:
            data = f.read()
            cityinitial="w"
    else:
        print("There is no data about the city you entered, please enter Chicago, New York, or Washington.\n")
    return data,cityinitial


def get_time_period():
    month_day = input(
        'Would you like to filter the data by month, day, or not at all? Type "none" for no time filter.\n')
    return month_day


def get_month():
    month = input('Which month? January, February, March, April, May, or June?\n')
    return month


def get_day():
    day = input('Which day?\n')
    return day


def popular_month(city,cityinitial):
    ## month is an empty dictionary
    months = {}
    ## first record contains column names, let's remove it
    a = city.splitlines()[1:]

    for i in a:
        times = i.split(',')[1] ## get date record
        ## record is different for different cities
        if (cityinitial == "w") or (cityinitial == "c"):
            time = datetime.strptime(times, '%m/%d/%Y %H:%M')
        else:
            time = datetime.strptime(times, '%m/%d/%Y %H:%M:%S')
        month = time.strftime("%B") ## get month name this way
        ## fill in the dictionary:
        if month in months:
            months[month] += 1
        else:
            months[month] = 1
    ## print the most popular month
    print("Most popular month to rent bikes is", max(months, key=months.get))


def weekdays():
    days = [0, 0, 0, 0, 0, 0, 0]
    name_days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    a = city.splitlines()
    for i in range(1, len(a)):
        b = int(str(a[i][0]) + str(a[i][1]) + str(a[i][2]) + str(a[i][3]))
        c = int(str(a[i][5]) + str(a[i][6]))
        d = int(str(a[i][8]) + str(a[i][9]))
        datee = datetime.date(b, c, d).weekday()
        if datee == 0:
            days[0] += 1
        elif datee == 1:
            days[1] += 1
        elif datee == 2:
            days[2] += 1
        elif datee == 3:
            days[3] += 1
        elif datee == 4:
            days[4] += 1
        elif datee == 5:
            days[5] += 1
        elif datee == 6:
            days[6] += 1
    i = 0
    for i in range(len(days)):
        if i == days.index(max(days)):
            print("Most popular day to rent bikes is", name_days[i])
        i += 1


def popular_hour():
    hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    name_hours = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14", "15", "16", "17",
                  "18", "19", "20", "21", "22", "23", "00"]
    a = city.splitlines()
    for i in a:
        times = str(i[11]) + str(i[12])
        if str(times) == "01":
            hours[0] += 1
        elif str(times) == "02":
            hours[1] += 1
        elif str(times) == "03":
            hours[2] += 1
        elif str(times) == "04":
            hours[3] += 1
        elif str(times) == "05":
            hours[4] += 1
        elif str(times) == "06":
            hours[5] += 1
        elif str(times) == "07":
            hours[6] += 1
        elif str(times) == "08":
            hours[7] += 1
        elif str(times) == "09":
            hours[8] += 1
        elif str(times) == "10":
            hours[9] += 1
        elif str(times) == "11":
            hours[10] += 1
        elif str(times) == "12":
            hours[11] += 1
        elif str(times) == "13":
            hours[12] += 1
        elif str(times) == "14":
            hours[13] += 1
        elif str(times) == "15":
            hours[14] += 1
        elif str(times) == "16":
            hours[15] += 1
        elif str(times) == "17":
            hours[16] += 1
        elif str(times) == "18":
            hours[17] += 1
        elif str(times) == "19":
            hours[18] += 1
        elif str(times) == "20":
            hours[19] += 1
        elif str(times) == "21":
            hours[20] += 1
        elif str(times) == "22":
            hours[21] += 1
        elif str(times) == "23":
            hours[22] += 1
        elif str(times) == "00":
            hours[23] += 1
    i = 0
    for i in range(len(hours)):
        if i == hours.index(max(hours)):
            print("Most popular hour to rent bikes is", name_hours[i])
        i += 1


def trip_duration():
    a = city.splitlines()
    num = int(len(a))
    duration_list = []
    for i in a:
        b = i.split(",")[2]
        duration_list.append(b)
    sum = 0
    for i in duration_list:
        if str(i) != "Trip Duration":
            sum += float(i)
    mean = int(sum / (len(duration_list) - 1))
    return sum, mean


def users():
    Customer = 0
    Subscriber = 0
    a = city.splitlines()
    for i in a:
        o=i.split(",")
        if str(o[5]) == "Customer":
            Customer += 1
        elif str(o[5]) == "Subscriber":
            Subscriber += 1
    print("Count of Customers is", Customer, "and count of Subscribers is", Subscriber)


def gender():
    genders = [0, 0]
    a = city.splitlines()
    for i in a:
       o=i.split(",")
       if str(o[6]) == "Female":
           genders[0] += 1
       elif str(o[6]) == "Male":
           genders[1] += 1
    print(genders[0], "of the customers are female and", genders[1], "are male")

def station():
    a = city.splitlines()
    dict1={}
    dict2={}
    for i in a:
        o=i.split(",")
        startname=str(o[3])
        endname=str(o[4])
        if startname in dict1:
            dict1[startname]+=1
        else:
            dict1.update({startname:1})
        if endname in dict2:
            dict2[endname]+=1
        else:
            dict2.update({endname:1})
    a= max(dict1.values())
    b=max(dict2.values())
    print ("Most popular start station is:", list(dict1.keys())[list(dict1.values()).index(a)])
    print("Most popular end station is:", list(dict2.keys())[list(dict2.values()).index(b)])

def oldest_youngest():
    a = city.splitlines()
    birth_year=[]
    for i in a:
        o=i.split(",")
        if len(o[-1]) == 6:
            birth_year.append(int(float(o[-1])))
    print("The oldest person's birth year is ", min(birth_year), "and the youngest person's birth year is ", max(birth_year))


city,initial = get_city()
time = get_time_period()

if time == 'month':
    month = input('Which month? January, February, March, April, May, or June?\n')
    weekdays()
    popular_hour()
    print('Total duration of trip is', trip_duration()[0], "minutes and average duration is", trip_duration()[1],
              "minutes")
    users()
    station()
    if initial != "w":
        gender()
        oldest_youngest()

elif time == 'day':
    day = input('Which day?\n')
    popular_hour()
    print('Total duration of trip is', trip_duration()[0], "minutes and average duration is", trip_duration()[1],
              "minutes")
    users()
    station()
    if initial != "w":
        gender()
        oldest_youngest()

elif time == 'none':
    popular_month()
    weekdays()
    popular_hour()
    print('Total duration of trip is', trip_duration()[0], "minutes and average duration is", trip_duration()[1],
             "minutes")
    users()
    station()
    if initial != "w":
        gender()
        oldest_youngest()



'''
if city == "Chicago" or city == "chicago" or city=="New York" or city=="new york":
    if time == 'month':
        month = input('Which month? January, February, March, April, May, or June?\n')
        weekdays()
        popular_hour()
        print('Total duration of trip is', trip_duration()[0], "minutes and average duration is", trip_duration()[1],
              "minutes")
        users()
        gender()
        station()
        oldest_youngest()

    elif time == 'day':
        day = input('Which day?\n')
        popular_hour()
        print('Total duration of trip is', trip_duration()[0], "minutes and average duration is", trip_duration()[1],
              "minutes")
        users()
        gender()
        station()
        oldest_youngest()

    elif time == 'none':
        popular_month()
        weekdays()
        popular_hour()
        print('Total duration of trip is', trip_duration()[0], "minutes and average duration is", trip_duration()[1],
              "minutes")
        users()
        gender()
        station()
        oldest_youngest()
elif city == "Washington" or city == "washington":
    if time == 'month':
        month = input('Which month? January, February, March, April, May, or June?\n')
        weekdays()
        popular_hour()
        print('Total duration of trip is', trip_duration()[0], "minutes and average duration is", trip_duration()[1],
              "minutes")
        users()
        station()

    elif time == 'day':
        day = input('Which day?\n')
        popular_hour()
        print('Total duration of trip is', trip_duration()[0], "minutes and average duration is", trip_duration()[1],
              "minutes")
        users()
        station()


    elif time == 'none':
        popular_month()
        weekdays()
        popular_hour()
        print('Total duration of trip is', trip_duration()[0], "minutes and average duration is", trip_duration()[1],
              "minutes")
        users()
        station()

'''

