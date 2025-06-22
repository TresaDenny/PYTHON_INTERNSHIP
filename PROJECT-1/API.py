import requests
import matplotlib.pyplot as plt
import seaborn as sns
import datetime

# Use your own API key here
API_KEY = '607e8d6e36f1a0e5c9f69ad1556dacae'
CITY = 'Mumbai'
URL = f'http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric'

# Fetch data from OpenWeatherMap API
response = requests.get(URL)
data = response.json()

# Extract date-time and temperature
dates = []
temps = []

for item in data['list']:
    dt = datetime.datetime.fromtimestamp(item['dt'])
    temp = item['main']['temp']
    dates.append(dt)
    temps.append(temp)

# Visualization using Seaborn
plt.figure(figsize=(12, 6))
sns.lineplot(x=dates, y=temps, marker='o')
plt.title(f"5-Day Temperature Forecast for {CITY}")
plt.xlabel("Date and Time")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.show()

