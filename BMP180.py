rom Adafruit_BMP085 import BMP085

# Initialise the BMP085 and use STANDARD mode (default value)
# bmp = BMP085(0x77, debug=True)
bmp = BMP085(0x77)

# Read the current Temp
#this will be used later on in the code to output a responce judged on the Temperature
temp = bmp.readTemperature()

# Read the current barometric pressure level
pressure = bmp.readPressure()

# To calculate altitude based on an estimated mean sea level pressure
# (1013.25 hPa) call the function as follows, but this won't be very accurate
altitude = bmp.readAltitude()

# To specify a more accurate altitude, enter the correct mean sea level
# pressure level.  For example, if the current pressure level is 1023.50 hPa
# enter 102350 since we include two decimal places in the integer value
# altitude = bmp.readAltitude(102350)

#Reading the temp and printing it
print ("Temperature: %.2f C" % temp)

#If ststement that will ouput a different phrase depending on the Temperature

Temp1 = int(bmp.readTemperature())

# if the temp is under 10 Degrees it will ouput that it is chilly 
if Temp1 < 10:
    print("Its a bit chilly outside!")
    
#if the temp is between 10 and 22 degrees it will output that it is a nice Temperature 
elif Temp1 <= 22:
    print("Its a Nice Temperature!")
    
#if it below 25 degrees it will output that it is a nice temperature 
elif Temp1 <= 25:
    print("Its Pretty Warm!")
    
# If the temperature is above 25 degrees it will ouput that it is hot outsde and to drink some water
else:   
    print("Wow, its HOT, Drink some water!")
    
print ("Pressure:    %.2f hPa" % (pressure / 100.0))
print ("Altitude:    %.2f" % altitude)
