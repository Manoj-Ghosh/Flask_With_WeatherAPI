from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = 'Your API Key'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    background_image = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            response = requests.get(BASE_URL, params={
                'q': city,
                'appid': API_KEY,
                'units': 'metric'
            })
            if response.status_code == 200:
                weather = response.json()
                weather_condition = weather['weather'][0]['main'].lower()
                # Map weather conditions to background images
                background_map = {
                    'clear': 'sunny.jpg',
                    'clouds': 'cloudy.jpg',
                    'rain': 'rainy.jpg',
                    'snow': 'snowy.jpg',
                    'storm': 'stormy.jpg',
                    'haze': 'haze.jpg'
                }
                background_image = background_map.get(weather_condition, 'default.jpg')  # default image if no match
            else:
                weather = {'message': 'City not found or API error.'}
    
    return render_template('index.html', weather=weather, background_image=background_image)

if __name__ == '__main__':
    app.run(debug=True)
