from flask import Flask, render_template
from flask_backend import weatherBlock

app = Flask(__name__)

weather_time_day = ["3am","6am","9am","12pm","3pm","6pm","9pm","12pm"]
weekly_data = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
dog_test = "Hi:8   Low:0   H:90%"
@app.route("/")
def homeDashboard():
    feels_like = weatherBlock.main()

    return render_template("index.html", feels_like=feels_like,
                           weather_time_day=weather_time_day,weekly_data=weekly_data, dog_test=dog_test)

if __name__ == '__main__':
    app.run(debug=True)
