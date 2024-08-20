from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = '85bb01ad3a213287e55a2d7156c2cc7b'
BASE_URL = 'http://api.openweathermap.org/data/2.5/weather'

@app.route('/', methods=['GET', 'POST'])
def index():
    weather = None
    var = False
    background_image = None
    if request.method == 'POST':
        city = request.form.get('city')
        if city:
            response = requests.get(BASE_URL, params={
                'q': city,
                'appid': API_KEY,
                'units': 'metric'
            })
            print(response.status_code)
            #if response.status_code != 200:

            if response.status_code == 200:
               weather = response.json()
               print(weather)
               var = True
                
                
               weather_condition = weather['weather'][0]['main'].lower()
                # Map weather conditions to background images
               background_map = {
                        'clear': 'sunny.jpg',
                        'clouds': 'cloudy.jpg',
                        'rain': 'rainy.jpg',
                        'snow': 'snowy.jpg',
                        'storm': 'stormy.jpg',
                        'haze': 'haze.jpg',
                        'mist':'mist.jpg'
                    }
               background_image = background_map.get(weather_condition, 'default.jpg')  # default image if no match
            else:
                weather = {'message': 'City not found or API error.'}
                background_image = 'thank_you.jpg'
                
            
    
    return render_template('index.html',var = var, weather=weather, background_image=background_image)

if __name__ == '__main__':
    app.run(debug=True)
