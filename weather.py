
import pyowm

owm = pyowm.OWM('21af4d40372f3029b260e9c76cddfcc7')  # You MUST provide a valid API key

# Search for current weather in London (Great Britain)
observation = owm.weather_at_place('Mumbai,India')
w = observation.get_weather()
#print(str(w.get_wind()))
#print(w.get_humidity())
b=w.get_temperature('celsius')
print(b)