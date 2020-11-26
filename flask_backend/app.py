from flask import Flask, render_template
from flask_backend import weatherBlock

app = Flask(__name__)

weekly_data = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
dog_test = "Hi:8   Low:0   H:90%"
@app.route("/")
def homeDashboard():
    feels_like = weatherBlock.main()

    return render_template("index.html", feels_like_temp=feels_like[0], feels_like_time=feels_like[1]
                           ,weekly_data=weekly_data, dog_test=dog_test)

if __name__ == '__main__':
    app.run(debug=True)
