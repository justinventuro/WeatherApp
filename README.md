# WeatherApp
Skills Used:<br>
-Flask Library<br>
-JSON Formatting<br>
-API calls and functions<br>
(Google Geocode API and OWN API)<br>
-HTML Templates (STATIC)<br>

This project uses 2 APIs (Google and OWN) to give accurate location and weather data using FLASK as a framework. The user enters their desierd loation and then weather and location data are returned. <br>
This project is commonly done with just the weather
, but this has it problems. With just the weather API you can only input a city for the weather, nothing more specific.
To solve this problem I integrated the Googel API. How it works is, the user inputs the location they would like the weather for and it is sent through
the Google API. The JSON data is combed through to find which city this location resides in. This city is sent then sent into the OWN API and the 
weather data for the city is returned.
