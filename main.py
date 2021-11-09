import json
from flask import Flask, render_template, request
import requests
import setting


app = Flask(__name__)
app.config['SECRET_KEY'] = b'm\x00?\xb2\xbe\x87\xd8\xea\xb2\xf9@\xc3\xa5u\x18\xd5'


class User_info(object):
    def __init__(self, city):
        self.city = city


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/result')
def Connect_api():
    url = "https://weatherapi-com.p.rapidapi.com/forecast.json"

    user_form = User_info(request.args.get('city'))

    querystring = {"q": user_form.city, "days": "3"}
    headers = {
        'x-rapidapi-key': setting.key,
        'x-rapidapi-host': setting.host
    }
    response = requests.request("GET", url, headers=headers, params=querystring)
    weather = json.loads(response.text)
    region = weather['location']['region']
    localtime = weather['location']['localtime']
    temp = weather['current']['temp_c']
    return render_template('temperature.html', region=region, localtime=localtime, temp=temp)


if __name__ == '__main__':
    app.run(debug=True)

