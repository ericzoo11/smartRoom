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


def temp_throughout_day(data):
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

    return temp_list, time_list, current_temp, current_forecast, selector


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
    temp_throughday = temp_throughout_day(data_API())
    day_temp = unit_conversion(temp_throughday[0])
    day_timestamp = time_extract(temp_throughday[1])
    current_temp = round(temp_throughday[2]-273.15)
    current_forecast = temp_throughday[3]
    forcast_selector = temp_throughday[4]

    return day_temp, day_timestamp, current_temp, current_forecast


# print("the size of list", len(test))

# dog = unit_conversion(test)
#print(*test2, sep=", ")
test2 = data_API()
print(json.dumps(test2, indent=4, sort_keys=True))

# print(type(y))
# print(round(y[0]), y[1], round(y[2]), y[3])
