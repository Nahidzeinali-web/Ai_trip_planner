# Import necessary libraries
import os
from utils.weather_info import WeatherForecastTool  # Custom module to handle weather data retrieval
from langchain.tools import tool  # LangChain decorator to define tools
from typing import List
from dotenv import load_dotenv  # For loading environment variables from a .env file

# Define a class to wrap weather-related tools
class WeatherInfoTool:
    def __init__(self):
        # Load environment variables from the .env file
        load_dotenv()
        # Retrieve the OpenWeatherMap API key from environment variables
        self.api_key = os.environ.get("OPENWEATHERMAP_API_KEY")
        # Instantiate the weather service tool with the API key
        self.weather_service = WeatherForecastTool(self.api_key)
        # Setup tools and store them in a list
        self.weather_tool_list = self._setup_tools()
    
    def _setup_tools(self) -> List:
        """Setup all tools for the weather forecast tool"""

        @tool
        def get_current_weather(city: str) -> str:
            """
            Tool to get current weather for a given city.
            
            Args:
                city (str): Name of the city.

            Returns:
                str: Weather description with temperature and condition.
            """
            # Call the weather service to fetch current weather data
            weather_data = self.weather_service.get_current_weather(city)
            if weather_data:
                # Extract temperature and weather description
                temp = weather_data.get('main', {}).get('temp', 'N/A')
                desc = weather_data.get('weather', [{}])[0].get('description', 'N/A')
                return f"Current weather in {city}: {temp}°C, {desc}"
            return f"Could not fetch weather for {city}"
        
        @tool
        def get_weather_forecast(city: str) -> str:
            """
            Tool to get weather forecast for a given city.
            
            Args:
                city (str): Name of the city.

            Returns:
                str: Multi-day forecast summary with temperatures and descriptions.
            """
            # Call the weather service to fetch forecast data
            forecast_data = self.weather_service.get_forecast_weather(city)
            if forecast_data and 'list' in forecast_data:
                forecast_summary = []
                # Loop through forecast list and collect date, temperature, and weather condition
                for i in range(len(forecast_data['list'])):
                    item = forecast_data['list'][i]
                    date = item['dt_txt'].split(' ')[0]
                    temp = item['main']['temp']
                    desc = item['weather'][0]['description']
                    forecast_summary.append(f"{date}: {temp} degree celcius , {desc}")
                return f"Weather forecast for {city}:\n" + "\n".join(forecast_summary)
            return f"Could not fetch forecast for {city}"
    
        # Return both tools as a list
        return [get_current_weather, get_weather_forecast]
