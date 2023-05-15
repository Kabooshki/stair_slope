import serial
import time

# Open a serial connection to the Arduino
ser = serial.Serial('COM6', 9600)  # Replace '/dev/ttyUSB0' with the appropriate serial port

# Function to send step commands to the Arduino
def send_steps(motor, steps):
    command = f"{motor}:{steps}\n"
    ser.write(command.encode())

# Control each motor
try:
    while True:
        # Control motor 1
        send_steps(1, 200)  # Adjust the number of steps as needed
        time.sleep(2)  # Wait for the motor to finish before moving to the next motor

        # Control motor 2
        send_steps(2, 300)  # Adjust the number of steps as needed
        time.sleep(2)

        # # Control motor 3
        # send_steps(3, 400)  # Adjust the number of steps as needed
        # time.sleep(1)

except KeyboardInterrupt:
    ser.close()

