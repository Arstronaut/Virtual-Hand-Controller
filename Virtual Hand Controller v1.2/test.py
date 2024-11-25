from alpaca.telescope import Telescope, TelescopeAxes
import time

T = Telescope('localhost:32323', 0)  # Local Omni Simulator

# Ensure the telescope is connected
if not T.Connected:
    T.Connected = True
    if T.Connected:
        print(f'Connected to {T.Name}')
        print(T.Description)
        T.Tracking = True
        print("Tracking is enabled")
    else:
        print("Failed to connect to the telescope.")
        exit()

try:
    rate=-2

    print("Attempting to move telescope.")
    T.MoveAxis(TelescopeAxes.axisSecondary, Rate=rate)  # Attempt movement with low rate
    print("Telescope is moving")

    time.sleep(10)  # Shorter duration for testing

    # Stop movement
    print("Stopping movement.")
    T.MoveAxis(TelescopeAxes.axisSecondary, Rate=0)
    print("Movement stopped.")

except AttributeError as e:
    print("The MoveAxis function or required property is not available on this simulator.")
except Exception as e:
    print(f"Error during movement: {e}")
    raise

finally:
    # Disconnect if connected
    if T.Connected:
        time.sleep(5)
        T.Connected = False
    print("Telescope disconnected.")
