from flask import Flask, render_template
from flask_backend import weatherBlock

#Global Variables
week_images = []
app = Flask(__name__)

@app.route("/")
def homeDashboard():
    day_data = weatherBlock.main()

    week_forecast = day_data[7]
    forecast_length = len(week_forecast)

    for i in range(forecast_length):
        temp = week_forecast[i]
        if temp == "Clouds":
            image = "static/images/259207-200.png"
        elif temp == "Rain":
            image = "static/images/Unknown.png"
        elif temp == "Snow":
            image = "static/images/snowflakes_PNG7577.png"
        else:
            image = "static/images/pngegg.png"
        week_images.append(image)

    forecast_image_current = current_forcast_image(day_data[3])


    return render_template("index.html", day_temps=day_data[0], day_timestamps=day_data[1], current_temp=day_data[2],
                           current_forecast=day_data[3], hi_low_of_day=day_data[4], weekday_strings=day_data[5],
                           weekday_data=day_data[6], location=day_data[8],week_images=week_images,
                           forecast_image_current=forecast_image_current)


if __name__ == '__main__':
    app.run(debug=True)


def current_forcast_image(dog):

    temp = dog
    if temp == "Clouds":
        image = "static/images/259207-200.png"
    elif temp == "Rain":
        image = "static/images/Unknown.png"
    elif temp == "Snow":
        image = "static/images/snowflakes_PNG7577.png"
    else:
        image = "static/images/pngegg.png"

    return image