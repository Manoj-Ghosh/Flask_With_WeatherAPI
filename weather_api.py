from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# Replace 'your_api_key' with your actual OpenWeatherMap API key
API_KEY = 'Past your API Keys Here'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            response = requests.get(BASE_URL, params={
                'q': city,
                'appid': API_KEY,
                'units': 'metric'  # For temperature in Celsius
            })
            if response.status_code == 200:
                weather = response.json()
            else:
                weather = {'message': 'City not found or API error.'}
    
    return render_template('index.html', weather=weather)

if __name__ == '__main__':
    app.run(debug=True)
