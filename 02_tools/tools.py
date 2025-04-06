import requests
from typing import Dict, Optional
from dotenv import load_dotenv
import os 
from agents import function_tool

load_dotenv()

# get api_key 
api_key = os.getenv("weather_api_key")

@function_tool
def get_current_weather(location: str) -> Optional[Dict]:
    """
    Get current weather data from WeatherAPI.com
    
    Args:
        api_key (str): Your WeatherAPI API key
        location (str): Location name or coordinates (e.g., 'London' or '48.8567,2.3508')
        
    Returns:
        Optional[Dict]: Weather data dictionary or None if request fails
    """
    url = "https://api.weatherapi.com/v1/current.json"
    
    headers = {
        "Content-Type": "application/json"
    }
    
    params = {
        "key": api_key,
        "q": location
    }
    
    try:
        response = requests.post(url, headers=headers, params=params)
        response.raise_for_status()  # Raise exception for non-200 status codes
        if response:
            current = response.json().get('current', {})
            #print (f"Temperature: {current.get('temp_c')}°C")
            return (f"Temperature: {current.get('temp_c')}°C")
        
    except requests.exceptions.RequestException as e:
        print(f"Error making API request: {e}")
        return None


#get_current_weather("New York")
