from flask import Flask, render_template
from flask_backend import weatherBlock

app = Flask(__name__)

weather_time_day = ["3am","6am","9am","12pm","3pm","6pm","9pm","12pm"]

@app.route("/")
def homeDashboard():
    feels_like = weatherBlock.main()

    return render_template("index.html", feels_like=feels_like,
                           weather_time_day=weather_time_day)

if __name__ == '__main__':
    app.run(debug=True)
