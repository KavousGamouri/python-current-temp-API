from abc import ABC, abstractmethod

class WeatherAPIBase(ABC):
    def __init__(self, city):
        
        self.city = city


    @abstractmethod
    def get_current_temperature(self):
        pass