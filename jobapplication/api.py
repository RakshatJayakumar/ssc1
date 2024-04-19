import requests

def get_random_fact():
    url = "https://ggv0l9zhxj.execute-api.eu-west-1.amazonaws.com/timedate/timedate"
    response = requests.get(url)
    if response.status_code == 200:
        fact = response.content.decode('utf-8')  
        return fact
    else:
        return "Failed to fetch random fact"

def get_weather(city):
    url = "http://x22203389scapp-env.eba-z5az2ytx.ap-south-1.elasticbeanstalk.com/weather/today"
    params = {"city": city}
    response = requests.get(url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        if 'main' in weather_data and 'temp' in weather_data['main'] and 'humidity' in weather_data['main']:
            temperature = weather_data['main']['temp']
            humidity = weather_data['main']['humidity']
            weather = weather_data['weather'][0]['description']
            return {'temperature': temperature, 'humidity': humidity, 'weather': weather}
        else:
            return None
    else:
        return None
        
def get_currency_conversion(source_currency, amount, target_currency):
    url = "https://f44dxfgsya.execute-api.eu-west-2.amazonaws.com/default/convert"
    payload = {
        "source_currency": source_currency,
        "amount": amount,
        "target_currency": target_currency
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        conversion_data = response.json()
        return conversion_data
    else:
        return None