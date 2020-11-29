import requests
import json

# global variables
current = 0
next = 1

def unit_conversion(temp_list):
    temp1 = []
    for i in temp_list:
        i -= 273.15
        temp1.append(round(i))
    return temp1


def data_API():
    response = requests.get(
        'http://api.openweathermap.org/data/2.5/forecast?q=Ottawa&appid=64fb5d61d627d52970a5fa0c0f689a0f')
    json_data = json.loads(
        response.text)  # using json.loads() method will parse the JSON string into a Python dictionary
    return json_data


def temp_of_week(data):
    temp_list = []  # initializing list

    for i in range(0, 6, 1):
        day_temp = data['list'][i]['main']['temp']
        temp_list.append(day_temp)

    return temp_list


def data_through_day(data):
    temp_list = []  # initializing list
    time_list = []

    # get temp throughout day
    for i in range(0, 8, 1):
        day_temp = data['list'][i]['main']['temp']
        temp_list.append(day_temp)

    # get corresponding times to temperature
    for i in range(0, 8, 1):
        date = data['list'][i]['dt_txt']
        time_list.append(date)

    # get current temperature
    current_temp = data['list'][0]['main']['temp']

    current_forecast = data['list'][0]['weather'][0]['description']

    selector = data['list'][0]['weather'][0]['main']

    date_hold = data['list'][0]['dt_txt']
    date_hold = date_hold[0:10]

    hi_low_list = hi_low(date_hold, data)

    return temp_list, time_list, current_temp, current_forecast, selector, hi_low_list


def parse_data(data):
    # get current temperature and convert to celcius
    current_temp = data['list'][current]['main']['temp']
    current_temp = unit_conversion(current_temp)

    current_forecast = data['list'][current]['weather'][current]['main']

    # get current feels like temperature and convert to celcius
    feels_like = data['list'][current]['main']['feels_like']
    feels_like = unit_conversion(feels_like)

    current_humidity = data['list'][current]['main']['humidity']

    # getting the current temp of the next day
    next_day2 = data['list'][next]['main']['temp']
    next_day2 = unit_conversion(next_day2)

    return current_temp, current_forecast, feels_like, current_humidity, next_day2


def data_through_week(data):

    dates_list = []
    day1_list = []
    day2_list = []
    day3_list = []
    day4_list = []
    day5_list = []

    list_len = len(data['list'])

    for i in range(list_len):
        date = data['list'][i]['dt_txt']
        date = date[0:10]
        dates_list.append(date)

    # removes repeated dates in list
    dates_list = list(dict.fromkeys(dates_list))

    # day 1
    day1 = dates_list[0]
    day1_list = hi_low(day1, data)

    # day 2
    day2 = dates_list[1]
    day2_list = hi_low(day2, data) 

    # day 3
    day3 = dates_list[2]
    day3_list = hi_low(day3, data)

    # day 4
    day4 = dates_list[3]
    day4_list = hi_low(day4, data)

    # day 5
    day5 = dates_list[4]
    day5_list = hi_low(day5, data)

    return day1_list, day2_list, day3_list, day4_list, day5_list


def hi_low(current_date, data):
    hi_list = [] # list to hold high values of the week
    low_list = [] # list to hold low values of the week

    list_len = len(data['list'])

    for i in range(list_len):
        dates = data['list'][i]['dt_txt']
        if current_date in dates:
            hi_temp = data['list'][i]['main']['temp_max']
            low_temp = data['list'][i]['main']['temp_min']
            hi_list.append(hi_temp)
            low_list.append(low_temp)

    hi_val = round(max(hi_list) - 273.15)
    low_val = round(min(low_list) - 273.15)

    return hi_val, low_val


def time_extract(time_list):
    new_list = []
    for i in time_list:
        string = i
        last_chars = string[-8:]
        if last_chars == "03:00:00":
            last_chars = "3am"
        elif last_chars == "06:00:00":
            last_chars = "6am"
        elif last_chars == "09:00:00":
            last_chars = "9am"
        elif last_chars == "12:00:00":
            last_chars = "12pm"
        elif last_chars == "15:00:00":
            last_chars = "3pm"
        elif last_chars == "18:00:00":
            last_chars = "6pm"
        elif last_chars == "21:00:00":
            last_chars = "9pm"
        elif last_chars == "00:00:00":
            last_chars = "12am"

        new_list.append(last_chars)

    return new_list


def main():
    temp_throughday = data_through_day(data_API())
    day_temp = unit_conversion(temp_throughday[0])
    day_timestamp = time_extract(temp_throughday[1])
    current_temp = round(temp_throughday[2]-273.15)
    current_forecast = temp_throughday[3]
    forcast_selector = temp_throughday[4]
    hi_low_of_day = temp_throughday[5]

    return day_temp, day_timestamp, current_temp, current_forecast, hi_low_of_day,


test = data_through_week((data_API()))

#print(test[0])
#print(test[1])
# dog = unit_conversion(test)
print(*test, sep=", ")
#print(*test[1], sep=", ")
#test2 = data_API()
#print(json.dumps(test2, indent=4, sort_keys=True))

# print(type(y))
# print(round(y[0]), y[1], round(y[2]), y[3])
