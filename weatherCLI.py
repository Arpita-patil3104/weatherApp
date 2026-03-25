import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")


cities = [
    "Pune", "Mumbai", "Delhi", "Bangalore",
    "Hyderabad", "Chennai", "Kolkata", "Jaipur"
]

def display_menu():

    print("\nSelect a city:\n")
    for i, city in enumerate(cities, start=1):
        print(f"{i}. {city}")
    print("\nOr type a city name manually.")
    print("Press Enter for default (Pune)\n")


def get_city_choice():
    user_input = input("Enter choice: ").strip()

   
    if user_input == "":
        return "Pune"

    
    if user_input.isdigit():
        index = int(user_input) - 1
        if 0 <= index < len(cities):
            return cities[index]
        else:
            print("Invalid number. Defaulting to Pune.")
            return "Pune"

  
    return user_input.title()


def get_weather(city):
    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params)
        data = response.json()

        if data.get("cod") != 200:
            print("❌ City not found. Try again.")
            return None

        weather = {
            "city": data["name"],
            "temp": data["main"]["temp"],
            "description": data["weather"][0]["description"].title(),
            "humidity": data["main"]["humidity"],
            "wind_speed": round(data["wind"]["speed"] * 3.6, 2)  # m/s → km/h
        }

        return weather

    except Exception as e:
        print("⚠️ Error fetching data:", e)
        return None


def display_weather(weather):
    print("\n---------------------------")
    print(f" Weather in {weather['city']}")
    print("---------------------------")
    print(f"Temperature : {weather['temp']}°C")
    print(f"Condition   : {weather['description']}")
    print(f"Humidity    : {weather['humidity']}%")
    print(f"Wind Speed  : {weather['wind_speed']} km/h")
    print("---------------------------\n")


def main():
    display_menu()
    city = get_city_choice()
    weather = get_weather(city)

    if weather:
        display_weather(weather)


if __name__ == "__main__":
    main()
