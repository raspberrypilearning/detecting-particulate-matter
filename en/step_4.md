## Design

Unlike the humidity/temperature sensor you used in the first project of this pathway, the SDS011 Particulate Matter Sensor connects to your Raspberry Pi via the USB ports.

In your research you might have discovered that the SDS011 sensor sends 10 bytes of data in a packet to your Raspberry Pi, via the serial bus. However, within that packet, the data you need is in the dataframe, which is sent in bytes 2 through to 7.

In particular, you are interested in bytes 2 and 3 for the 2.5µm particles and bytes 4 and 5 for the 10µm particles.

Your program will have to read these bytes over a set time period, and convert them to integers. After that it will need to display and save the data as well as uploading the data to an IOT platform.

