from flask import Flask, render_template
from flask_backend import weatherBlock

app = Flask(__name__)

weekly_data = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
dog_test = "Hi:8   Low:0   H:90%"
@app.route("/")
def homeDashboard():
    day_data = weatherBlock.main()

    return render_template("index.html", day_temps=day_data[0], day_timestamps=day_data[1],
                           current_temp=day_data[2], current_forecast=day_data[3], dog_test=dog_test,
                           weekly_data=weekly_data, hi_low_of_day=day_data[4], weekday_strings=day_data[5],
                           weekday_data=day_data[6])

if __name__ == '__main__':
    app.run(debug=True)
