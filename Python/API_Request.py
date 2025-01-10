# Import the requests library to make HTTP requests.
import requests

# Define a function to fetch weather data for a given city.
def fetch_weather(city):
    # Format the URL with the city name and metric units.
    url = f'https://wttr.in/{city}?m'
    try:
        # Send the GET request to fetch the weather data
        response = requests.get(url)
        response.raise_for_status()

        # Return the plain text weather data
        return response.text
    except requests.exceptions.RequestException as e:
        return f"An error occurred: {e}"

# Define the main function to handle user interaction.
def main():
    first_prompt = True
    while True:
        # Choose prompt based on whether it's the first or subsequent iterations
        if first_prompt:
            city = input("Enter the city name (or type 'exit' to quit): ").strip()
            first_prompt = False
        else:
            city = input("Enter another city name (or type 'exit' to quit): ").strip()
        
        # Check if the user wants to exit.
        if city.lower() == "exit":    
            print("Thank you!")
            break

        # Check if the input is not empty.
        if city:    
            print("\nFetching weather data...\n")
            # Fetch and display weather data
            weather_data = fetch_weather(city)
            print(weather_data)
        else:
            print("Please enter a valid city name!")

# Run the main function when the script is executed directly.
if __name__ == "__main__":
    main()