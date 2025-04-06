from dataclasses import dataclass
from agents import RunContextWrapper, function_tool

@dataclass
class User:
    name : str
    weather_preference : str
    id : int 

@function_tool
def get_user_preference(wrapper : RunContextWrapper[User]) -> str:

    """This function will get the user name and  weather preference from the context"""
    
    name = wrapper.context.name
    preference = wrapper.context.weather_preference

    return f"User : {name} prefers {preference} weather"

