import requests
from base import WeatherAPIBase



class OpenWeatherMap(WeatherAPIBase):
    def __init__(self, latitude, longitude, **kwargs):
        self.latitude = latitude
        self.longitude = longitude
        self.API_KEY = kwargs.get('API_KEY')


    def get_current_temperature(self):
        params = {'lat': self.latitude, 'lon': self.longitude, 'appid': self.API_KEY}
        base_url = requests.get('https://api.openweathermap.org/data/2.5/weather',params=params)
        result = base_url.json()
        result_json = result['main']['temp'] 
        result_json -= 273.15
        return result_json
    



class OpenMeteo(WeatherAPIBase):
    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude
        


    def get_current_temperature(self):
        params = {'latitude': self.latitude, 'longitude': self.longitude, 'current_weather':True}
        result = requests.get('https://api.open-meteo.com/v1/forecast', params=params)
        result_json = result.json()
        return result_json['current_weather']['temperature']
    
    
    
latitude = 35.69
longitude = 51.42


if __name__ == '__main__':
    open_weather_obj = OpenWeatherMap(latitude, longitude, API_KEY='ed1ad0d935af4ad100adf852fa660e29')
    temp = open_weather_obj.get_current_temperature()
    print(f'Current temperature from openwaether is ==> {temp}')

    open_meteo_obj = OpenMeteo(latitude, longitude)
    temp = open_meteo_obj.get_current_temperature()
    print(f'Current temperature from openmeteo is ==> {temp}')
