## Develop - Record your data to a csv

It would be helpful to store all the data from the sensors in a more permanent way than the animated graph. To do this you can write the data to a csv sheet.

[[[generic-python-writing-csv]]]

--- task ---

Write a new function to write data to a csv. Call this new function within your `collect_data()` function.

Here's an outline of what your function should contain.

```python
from csv import writer

def write_data(time, pm_two_five, pm_ten):
	
	#Open the csv file in append mode
	
	#Create a writer object
	
	#Write a row of data to include time, pm_two_five and pm_ten values
```

--- /task ---






