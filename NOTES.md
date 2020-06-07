# Notes from the LEGO&reg; API

## Version 1.0.0

Section 4.2.5 is titled Gyroscopic Sensor, but the Python class name is listed as GyroSensor. GyroSensor is the correct name, so that is the name used in the package.

According to the API, the ev3brick.display.image method should accept a string for the file_name parameter. In this package, the method will accept either a string or an ImageFile value (which would be a string if weaker typings were enforced).
