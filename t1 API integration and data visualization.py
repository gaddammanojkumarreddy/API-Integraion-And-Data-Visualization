import requests
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def fetch_weather_data(city, api_key):
    url = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    response.raise_for_status()  # Raise error if request fails
    return response.json()

def parse_weather_data(data):
    forecast_list = data['list']
    weather_data = {
        'datetime': [entry['dt_txt'] for entry in forecast_list],
        'temperature': [entry['main']['temp'] for entry in forecast_list],
        'humidity': [entry['main']['humidity'] for entry in forecast_list],
        'wind_speed': [entry['wind']['speed'] for entry in forecast_list]
    }
    df = pd.DataFrame(weather_data)
    df['datetime'] = pd.to_datetime(df['datetime'])
    return df

def visualize_weather(df, city):
    plt.figure(figsize=(15, 10))
    sns.set(style="darkgrid")

    # Temperature Plot
    plt.subplot(3, 1, 1)
    sns.lineplot(x='datetime', y='temperature', data=df, color='tomato')
    plt.title(f'Temperature Forecast for {city}')
    plt.xlabel('Date')
    plt.ylabel('Temperature (°C)')

    # Humidity Plot
    plt.subplot(3, 1, 2)
    sns.lineplot(x='datetime', y='humidity', data=df, color='blue')
    plt.title('Humidity Forecast')
    plt.xlabel('Date')
    plt.ylabel('Humidity (%)')

    # Wind Speed Plot
    plt.subplot(3, 1, 3)
    sns.lineplot(x='datetime', y='wind_speed', data=df, color='green')
    plt.title('Wind Speed Forecast')
    plt.xlabel('Date')
    plt.ylabel('Wind Speed (m/s)')

    plt.tight_layout()
    plt.show()

def main():
    city = 'Hyderabad'  # You can change the city
    api_key = 'YOUR_API_KEY'  # Replace with your OpenWeatherMap API key

    try:
        data = fetch_weather_data(city, api_key)
        df = parse_weather_data(data)
        visualize_weather(df, city)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    main()
