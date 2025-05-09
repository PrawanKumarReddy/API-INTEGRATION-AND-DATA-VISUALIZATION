import requests  # Import the 'requests' library to handle HTTP requests
import matplotlib.pyplot as plt  # Import 'matplotlib' to create plots

# we have to enter the API Key and City
api_key = '5a8e26ccea0e7a8a399f7f60e26096e0'  # Your API key from OpenWeatherMap
city= input("Enter the city name:") # You can change this to any city you want to get weather data for.

#  Construct the API URL
# Here, we are building the URL to query OpenWeatherMap API for the current weather in a specified city/location.
# The units=metric parameter will return the temperature in Celsius.
url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'

# Making the HTTP Request
# We are sending a GET request to the OpenWeatherMap API using the constructed URL.
response = requests.get(url)

# Step1: Integrating the data
# Check the Response Status
# If the API request is successful (status code 200), proceed to extract data.
if response.status_code == 200:
    #  Extracting Data from the Response
    # Convert the JSON response into a Python dictionary for easier data extraction.
    data = response.json()

    # Extracting specific pieces of weather data:
    temperature = data['main']['temp']  # Temperature in Celsius
    humidity = data['main']['humidity']  # Humidity percentage
    weather_description = data['weather'][0]['description']  # Description of the weather condition (e.g., "overcast clouds")
    
    # Print the extracted data to the console for verification:
    print(f"City: {city}")
    print(f"Temperature: {temperature}°C")  # Display temperature
    print(f"Humidity: {humidity}%")  # Display humidity
    print(f"Weather: {weather_description}")  # Display weather description
    
    # Step2: Visualization using Matplotlib
    # We will create a bar chart showing the temperature and humidity values.
    
    # Labels for the x-axis
    labels = ['Temperature (°C)', 'Humidity (%)']
    # Corresponding values for the bar chart
    values = [temperature, humidity]
    
    # Create a figure for the plot, setting the figure size
    plt.figure(figsize=(6, 4))
    
    # Create a bar chart with custom colors for the bars
    plt.bar(labels, values, color=['skyblue', 'lightgreen'])
    
    # Add a title to the chart
    plt.title(f"Weather Data for {city}")
    
    # Label the x-axis
    plt.xlabel("Parameters")
    
    # Label the y-axis
    plt.ylabel("Values")
    
    # Display the plot
    # Show the plot to the user.
    plt.show()

else:
    # If the status code is not 200, it means something went wrong (e.g., invalid API key).
    # Print the status code and error message to understand the issue.
    print(f"Failed to fetch data: {response.status_code}")
    print(response.text)  # Prints the error message returned by the API
