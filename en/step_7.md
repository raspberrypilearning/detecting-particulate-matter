## Develop - Read the sensor

Here is the datasheet for the SDS011 sensor.

[SDS011 datasheet](https://cdn-reichelt.de/documents/datenblatt/X200/SDS011-DATASHEET.pdf)

Scroll down to see the section on the UART Communication Protocol. You'll see a table with the following information.

| The number of bytes | Name           | Content         |
|---------------------|----------------|-----------------|
| 0                   | Message header | AA              |
| 1                   | Commander No.  | C0              |
| 2                   | DATA 1         | PM2.5 Low byte  |
| 3                   | DATA 2         | PM2.5 High byte |
| 4                   | DATA 3         | PM10 Low byte   |
| 5                   | DATA 4         | PM10 High byte  |
| 6                   | DATA 5         | ID byte 1       |
| 7                   | DATA 6         | ID byte 2       |
| 8                   | Check-sum      | Check-sum       |
| 9                   | Message tail   | AB              |

The SDS011 sends 10 bytes of data to the Raspberry Pi, each second using the [UART](https://en.wikipedia.org/wiki/Universal_asynchronous_receiver-transmitter) protocol.

The bytes we are interested in are at positions 2, 3, 4 and 5.

You can use the Python `Serial` library to fetch these bytes.

--- task ---

Open a terminal and type the following, to discover which port the SDS011 sensor is connected to.

```bash
dmesg | grep 'tty'
```

You should see a line in the response that reads something like:

```bash
usb 1-1.1: ch341-uart converter now attached to ttyUSB0
```

This is telling you that the SDS011 sensor is on `\dev\ttyUSB0`.

--- /task ---

--- task ---

Open up a text editor or your prefered Python IDE

To read data from the sensor, you can use the `pyserial` library.

[[[nix-python-reading-serial-data]]]

--- task ---

Use the `pyserial` library to read the bytes you are interested in.

| The number of bytes | Name           | Content         |
|---------------------|----------------|-----------------|
| 2                   | DATA 1         | PM2.5 Low byte  |
| 3                   | DATA 2         | PM2.5 High byte |
| 4                   | DATA 3         | PM10 Low byte   |
| 5                   | DATA 4         | PM10 High byte  |

Store the bytes as `low_two_five`, `high_two_five`, `low_ten` and `high_ten` It's a good idea to reset the the input buffer in between reads of the sensor.

--- /task ---

