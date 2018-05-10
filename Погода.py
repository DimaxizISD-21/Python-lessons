import pyowm

city = input('Какой город Вас интересует ?: ')

owm = pyowm.OWM('a13dfaf94cd27ebca43cecef90d9397a' , language='ru')
observation = owm.weather_at_place(city)
w = observation.get_weather()
temperature = w.get_temperature('celsius')['temp']

print("В городе " + city + " сейчас температура: " + str(temperature) + " по цельсию. ")
print("Также, в указанном городе " + w.get_detailed_status())
input("Нажмите Enter для завершения программы")