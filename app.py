from flask import Flask
import datetime

app = Flask(__name__)


@app.route('/')
def main_func():
    content = "<p>" + "Online @ " + str(datetime.datetime.now()) + "</p>"
    return content


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)
