## Discover

Why do we need to be concerned by the particulate matter in our air?

Conduct some research into the types of particulate matter that might exist in the air around you, and detail the potential health risks associated with particulate matter.

Use this document to record your findings.

And here are some links to online resources that you might find useful.





## Research
http://aqicn.org/media/
https://en.wikipedia.org/wiki/Air_quality_index

## Humidity and Temperature with DHT22
https://github.com/adafruit/Adafruit_Python_DHT

## Cloud
https://sense-iot.com/
https://io.adafruit.com/

## Setup
https://towardsdatascience.com/sensing-the-air-quality-5ed5320f7a56

### Define
Air quality is an issue, especially in urban areas. Monitor and warn people of AQI in their area

### Discover
Look into types of polution, but guide towards particulate matter.
Look into devices that can measure these values

### Design
Guided design of sensor housing. Sensor needs airflow, but Pi needs to be protected from rain.

### Decompose
- Connect sensor and test sensor
- Connect to a cloud platform
- Test upload to platform
- Create full script
- Automate runs
- Add to housing

### Develop
Basic instructions for each of the above, with some guidance and opportunities for independence

1. Connect up sensor, install libraries then have them using the documentation to get the pm2.5 and pm10 values
1. Choose a platform to upload to. Learners can choose and use documentation to figure out the API
1. Test uploading a small amount of data
1. Full script to automate upload of data once per minute. 
1. Humidity correction as an optional extra.
1. Design a housing
1. Create a housing and install

### Demonstrate
Publishing the available data for local use.
