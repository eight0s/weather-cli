# Weather CLI Tool 🌤️

A simple command-line application that fetches real-time weather data for any city using the OpenWeatherMap API.

## Features

- Get current weather conditions for any city worldwide
- Displays temperature, humidity, wind speed, and weather conditions
- Clean, user-friendly command-line interface
- Continuous search until user exits

## Technologies Used

- Python 3.11
- OpenWeatherMap API
- Requests library

## Installation

1. Clone this repository:
```bash
git clone https://github.com/eight0s/weather-cli.git
cd weather-cli
```

2. Create a virtual environment:
```bash
python -m venv venv
```

3. Activate the virtual environment:
- Windows: `venv\Scripts\activate`
- Mac/Linux: `source venv/bin/activate`

4. Install dependencies:
```bash
pip install requests
```

5. Get your free API key:
   - Sign up at [OpenWeatherMap](https://openweathermap.org/api)
   - Go to your account dashboard
   - Copy your API key

6. Open `weather.py` and replace the `API_KEY` variable with your own key:
```python
API_KEY = "your_api_key_here"
```

## Usage

Run the program:
```bash
python weather.py
```

Enter a city name when prompted:
```
Enter a city name (or 'quit' to exit): London
```

Type 'quit' to exit the program.

## Example Output
```
🌤️  Current Weather in London
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Temperature: 45.1°F
Feels like: 43.5°F
Conditions: Overcast
Humidity: 88%
Wind Speed: 3.7 mph
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Project Structure
```
weather-cli/
│
├── weather.py          # Main application file
├── README.md           # Project documentation
├── .gitignore          # Git ignore rules
└── venv/              # Virtual environment (not tracked)
```

## Learning Outcomes

This project helped me learn:
- Working with REST APIs
- Parsing JSON data
- Error handling in Python
- Creating interactive CLI applications
- Virtual environments and dependency management

## Future Improvements

- [ ] Add 5-day forecast
- [ ] Save favorite cities
- [ ] Support for multiple temperature units
- [ ] Add weather icons
- [ ] Export data to CSV
- [ ] Store API key in environment variable for better security

## License

This project is open source and available under the MIT License.

## Author

David ([eight0s](https://github.com/eight0s)) - First Year University Student

Built as part of learning Python and API integration.
https://roadmap.sh/projects/weather-api-wrapper-service
