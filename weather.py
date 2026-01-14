import requests

# OpenWeatherMap API configuration
API_KEY = "d0e954e7862d5123c4bf3a86a61b36f7"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    """
    Fetch and display current weather for a given city.
    
    Args:
        city (str): Name of the city to get weather for
    """
    # Set up API request parameters
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "imperial"  # Fahrenheit (use "metric" for Celsius)
    }
    
    # Make the API request
    response = requests.get(BASE_URL, params=params)
    
    # Handle errors
    if response.status_code != 200:
        print(f"❌ Error: Could not find weather for '{city}'")
        print("Please check the city name and try again.")
        return
    
    # Parse JSON response
    data = response.json()
    
    # Display weather information
    print(f"\n🌤️  Current Weather in {city.title()}")
    print("━" * 40)
    print(f"Temperature: {data['main']['temp']}°F")
    print(f"Feels like: {data['main']['feels_like']}°F")
    print(f"Conditions: {data['weather'][0]['description'].title()}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} mph")
    print("━" * 40 + "\n")

def main():
    """Main program loop for the Weather CLI."""
    print("🌍 Weather CLI Tool")
    print("=" * 40)
    print("Get current weather for any city worldwide!")
    
    while True:
        city = input("\nEnter a city name (or 'quit' to exit): ")
        
        # Exit condition
        if city.lower() == 'quit':
            print("👋 Thanks for using Weather CLI! Goodbye!")
            break
        
        # Validate input
        if city.strip() == "":
            print("❌ Please enter a valid city name.")
            continue
        
        # Get and display weather
        get_weather(city)

if __name__ == "__main__":
    main()