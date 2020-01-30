import serial
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from datetime import datetime

pmd = serial.Serial('/dev/ttyUSB0',
                    baudrate=9600,
                    parity=serial.PARITY_NONE,
                    stopbits=serial.STOPBITS_ONE)

# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

times = []
pm_two_five_data = []
pm_ten_data = []

# Initialize communication with TMP102
def collect_data():
    pmd.reset_input_buffer()
    data = pmd.read(10)
    low_two_five = data[2]
    high_two_five = data[3]
    low_ten = data[4]
    high_ten = data[5]
    pm_two_five = (high_two_five * 256 + low_two_five) / 10
    pm_ten = (high_ten * 256 + low_ten) / 10
    print(pm_two_five, pm_ten)
    return pm_two_five, pm_ten

# Add labels


# This function is called periodically from FuncAnimation
def animate(i, times, pm_two_five_data, pm_ten_data):
    # Read temperature (Celsius) from TMP102
    pm_two_five, pm_ten = collect_data()
    time = datetime.now()
    # Add y to list
    pm_two_five_data.append(pm_two_five)
    pm_ten_data.append(pm_ten)
    times.append(time)


    # Limit y list to set number of items
    ax.clear()
    plt.title('PM2.5 and PM10 levels over time')
    plt.xlabel('Time')
    plt.ylabel('PM values micro grams per cubic meter')
    #ax.set_ylim([0,2000])
    ax.plot(times, pm_two_five_data, label='2.5')
    ax.plot(times, pm_ten_data, label='10')
    plt.legend()
    fig.autofmt_xdate()


# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig,
    animate,
    fargs=(times, pm_two_five_data, pm_ten_data),
    interval=1000)

#plt.show()
ani.save('/home/pi/animation.gif', writer='imagemagick', fps=10)
