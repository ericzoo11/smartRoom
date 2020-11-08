from flask import Flask, render_template
import weatherBlock

app = Flask(__name__)


@app.route("/")
def homeDashboard():
    feels_like = weatherBlock.main()
    cat = weatherBlock.main()  # calling weatherBlock file
    dog = round(cat[0])
    dog1 = cat[1]
    dog2 = round(cat[2])
    dog3 = round(cat[3])
    dog4 = round(cat[4])
    return render_template("index.html", feels_like=feels_like, content="TESTING", content2=dog, content3=dog1,
                           content4=dog2,
                           content5=dog3,
                           content6=dog4)


if __name__ == '__main__':
    app.run(debug=True)
