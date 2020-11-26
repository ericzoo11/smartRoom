from flask import Flask, render_template
from flask_backend import weatherBlock

app = Flask(__name__)

weekly_data = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
dog_test = "Hi:8   Low:0   H:90%"
@app.route("/")
def homeDashboard():
    day_data = weatherBlock.main()

    return render_template("index.html", day_temps=day_data[0], day_timestamps=day_data[1],
                           current_temp=day_data[2], weekly_data=weekly_data, dog_test=dog_test)

if __name__ == '__main__':
    app.run(debug=True)
