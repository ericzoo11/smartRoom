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


def temp_of_day(data):
    temp_list = []  # initializing list

    for i in range(0, 8, 1):
        day_temp = data['list'][i]['main']['temp']
        temp_list.append(day_temp)
    return temp_list


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


def main():

    feels_like = unit_conversion(temp_of_day(data_API()))
    return feels_like

test = temp_of_day(data_API())
print("the size of list", len(test))

dog = unit_conversion(test)
print(*dog, sep=", ")

#est2 = data_API()
#print(json.dumps(test2, indent=4, sort_keys=True))

# print(type(y))
# print(round(y[0]), y[1], round(y[2]), y[3])
