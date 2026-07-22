"""
Simple Multi-Model AI Agent

Functions:
1. Weather(city)
2. Calculator(a, b)
3. Currency Converter(amount, rate)
"""

import re

# ---------------- Weather ----------------
def weather(city):
    weather_data = {
        "hyderabad": {"condition": "Cloudy", "temp": 30},
        "chennai": {"condition": "Cloudy", "temp": 35},
        "bangalore": {"condition": "Cloudy", "temp": 20},
        "mumbai": {"condition": "Cloudy", "temp": 24},
        "new delhi": {"condition": "Cloudy", "temp": 39},
        "kerala": {"condition": "Cloudy", "temp": 27},
        "new york": {"condition": "Cloudy", "temp": 20}
    }

    key = city.strip().lower()

    if key in weather_data:
        data = weather_data[key]
        return f"Weather in {city.title()}: {data['condition']}, {data['temp']}°C"

    return f"Weather not found for {city}"


# ---------------- Calculator ----------------
def calculator(a, b):
    result = {
        "Sum": a + b,
        "Subtraction": a - b,
        "Multiplication": a * b,
        "Division": a / b if b != 0 else "Cannot divide by zero"
    }
    return result


# ---------------- Currency Converter ----------------
def currency_converter(amount, rate):
    converted = amount * rate
    return round(converted, 2)


# ---------------- Request Handler ----------------
def handle_req(user_input):

    text = user_input.lower()

    # Weather
    if "weather" in text:
        match = re.search(r"weather\s*(?:in|for|at)?\s*([a-zA-Z\s]+)", text)

        if match:
            city = match.group(1).strip()
            return weather(city)
        else:
            return "Please provide a city name."

    # Calculator
    if any(word in text for word in
           ["calculate", "add", "subtract", "multiply", "divide"]):

        nums = re.findall(r"\d+", text)

        if len(nums) >= 2:
            a = int(nums[0])
            b = int(nums[1])
            return calculator(a, b)
        else:
            return "Provide two numbers. Example: calculate 10 and 40"

    # Currency Converter
    if "convert" in text or "exchange" in text:

        match = re.search(
            r"convert\s+(\d+(?:\.\d+)?)\s+at\s+rate\s+(\d+(?:\.\d+)?)",
            text
        )

        if match:
            amount = float(match.group(1))
            rate = float(match.group(2))
            return currency_converter(amount, rate)
        else:
            return "Example: convert 100 at rate 95.5"

    return "Sorry, I didn't understand your request."


# ---------------- Main Program ----------------
if __name__ == "__main__":

    sample_req = [
        "weather in Hyderabad",
        "calculate 25 and 69",
        "convert 100 at rate 95.5"
    ]

    print("Sample Outputs:\n")

    for req in sample_req:
        print("Request :", req)
        print("Response:", handle_req(req))
        print("-" * 40)

    while True:
        user_input = input("\nAsk something (or type exit): ")

        if user_input.lower() == "exit":
            print("Goodbye!")
            break

        print(handle_req(user_input))