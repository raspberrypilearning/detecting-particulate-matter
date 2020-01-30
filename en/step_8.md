## Develop - Calculate particulate matter concentrations

If you read the [datasheet for the sensor](https://cdn-reichelt.de/documents/datenblatt/X200/SDS011-DATASHEET.pdf) again, you should be able to find this section.

```
PM2.5 value: PM2.5 (μg /m3) = ((PM2.5 high byte * 256) + PM2.5 low byte) / 10
PM10  value: PM10  (μg /m3) = ((PM10  high byte * 256) + PM10  low byte) / 10
```

--- task ---

Perform these calculations on your `low_two_five`, `high_two_five`, `low_ten` and `high_ten` variables. Store the values as `pm_two_five` and `pm_ten`.

--- /task ---

--- task ---

Have your function return the `pm_two_five` and `pm_ten`.

```python
def collect_data():
	
	#Reset the input buffer
	
	#Read the data
	
	#Store the low and high bytes
	
	#Convert the bytes to integer PM values
	
	return pm_two_five, pm_ten
```

--- /task ---

