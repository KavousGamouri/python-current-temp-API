import requests
from base import WeatherAPIBase



class OpenWeatherMap(WeatherAPIBase):
    API_KEY = 'ed1ad0d935af4ad100adf852fa660e29'
    def __init__(self, city):
        self.city = city
        


    def get_current_temperature(self):
        base_url = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={OpenWeatherMap.API_KEY}')
        result = base_url.json()
        result_json = result['main']['temp'] 
        result_json -= 273.15
        return f'API from openweathermap.org ==> {result_json}'
    



class WeatherAPI(WeatherAPIBase):
    API_KEY = '3fa73faa1ec446cab5002311231807'
    def __init__(self, city):
        self.city = city
        


    def get_current_temperature(self):
        base_url = requests.get(f'https://api.weatherapi.com/v1/current.json?key={WeatherAPI.API_KEY}&q={self.city}')
        result = base_url.json()
        result_json = result['current']['temp_c'] 
        
        return f'API from weatherapi.com ==> {result_json}'
    
    



if __name__ == '__main__':
    open_weather_map = OpenWeatherMap('karaj')
    print(open_weather_map.get_current_temperature())

    weather_api = WeatherAPI('karaj')
    print(weather_api.get_current_temperature())