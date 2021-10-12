from pyowm import OWM
from pyowm.utils import config
from pyowm.utils import timestamps

# MY API KEY 
owm = OWM('3a044d2aad8cdb129980e2e28876c9a3')
mgr = owm.weather_manager()
def currentWeather():
    observation = mgr.weather_at_place("London,GB")
    w = observation.weather
    wind = w.wind()
    temperature = w.temperature('fahrenheit')
    return str(temperature) + str(wind)