# Seed
> Contains node files to run a MVP PFC derived from Original PFC. Refer to GYOF for running the MVP
A minimalistic code based on MVP - Open Agriculture, using python running on raspberry pi.
With cron as scheduler to call python files which includes 3 actuators ( LED , Exhaust Fan and Circulation Fan) ,as per the temperature and humidity from si7021 sensor using the thermostat file.

A Dashboard based on Dash by Plotly (open source ) is used for GUI of data and images from the 2 webcams.
Working:
Cron is the scheduler and call the thermostat file which maintains target temperature (Seed/Python/buildVariable.py) by switching on/off the Exhaust Fan
It also switches the Lights on / off at the specified time (Seed/scripts/Seed_cron.txt)
