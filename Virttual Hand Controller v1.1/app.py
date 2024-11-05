from flask import Flask, render_template, request, jsonify
from alpaca.telescope import Telescope, TelescopeAxes
import time

app = Flask(__name__)

# Initialize Telescope
T = Telescope('localhost:32323', 0)  # Local Omni Simulator
print(f'Connected to {T.Name}')
print(T.Description)
T.Tracking = True

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/message', methods=['POST'])
def receive_message():
    """Handle incoming messages and issue commands based on button presses."""
    data = request.get_json()  # Get JSON data
    direction = data.get('message') 
    rate = data.get('rate', 0)
    P_axis = TelescopeAxes.axisPrimary
    Sec_axis = TelescopeAxes.axisSecondary



    try:
        if direction == "up":
            T.MoveAxis(Sec_axis, rate)

        elif direction == "down":
            T.MoveAxis(Sec_axis, -rate)

        elif direction == "left":
             T.MoveAxis(P_axis, rate)

        elif direction == "right":
          T.MoveAxis(P_axis, -rate)  

        else:
            print("Unknown button direction")
            return jsonify(status="error", message="Unknown direction")

        return jsonify(status="success", message=f"Received {direction} command")

    except Exception as e:
        print(f"Error during processing: {e}")
        return jsonify(status="error", message="Error during processing")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)  # Disable reloader to avoid threading issues
