import requests

api_key = "your_api_key_here"

city = input("Enter city name: ")

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)
data = response.json()

description = data["weather"][0]["description"]
temp_kelvin = data["main"]["temp"]
temp_celsius = temp_kelvin - 273.15

print(f"Weather: {description}")
print(f"Temperature: {temp_celsius:.1f} °C")


