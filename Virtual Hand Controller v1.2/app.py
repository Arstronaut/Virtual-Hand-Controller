from flask import Flask, render_template, request, jsonify
from alpaca.telescope import Telescope, TelescopeAxes
import time

app = Flask(__name__)
maestro_flag = False

@app.route('/', methods=['GET'])
def index():
    flag = {'maestro' : maestro_flag}
    return render_template('index.html', flag=flag)

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
            if maestro_flag:
                print("KSpu")
                T.CommandString("KSpu", False)
                if rate == 0:
                    print("XXud")
                    T.CommandString("XXud", False)
                if rate == 1:
                    print("KSv1")
                    T.CommandString("KSv1", False)
                if rate == 2:
                    print("KSv2")
                    T.CommandString("KSv2", False)
                if rate == 3:
                    print("KSv3")
                    T.CommandString("KSv3", False)
                if rate == 4:
                    print("KSv4")
                    T.CommandString("KSv4", False)
            else:
                T.MoveAxis(Sec_axis, rate)

        elif direction == "down":
            if maestro_flag:
                print("KSpd")
                T.CommandString("KSpd", False)
                if rate == 0:
                    print("XXud")
                    T.CommandString("XXud", False)
                if rate == 1:
                    print("KSv1")
                    T.CommandString("KSv1", False)
                if rate == 2:
                    print("KSv2")
                    T.CommandString("KSv2", False)
                if rate == 3:
                    print("KSv3")
                    T.CommandString("KSv3", False)
                if rate == 4:
                    print("KSv4")
                    T.CommandString("KSv4", False)
            else:
                T.MoveAxis(Sec_axis, -rate)


        elif direction == "left":
             if maestro_flag:
                print("KSpl")
                T.CommandString("KSpl", False)
                if rate == 0:
                    print("XXlr")
                    T.CommandString("XXud", False)
                if rate == 1:
                    print("KSv1")
                    T.CommandString("KSv1", False)
                if rate == 2:
                    print("KSv2")
                    T.CommandString("KSv2", False)
                if rate == 3:
                    print("KSv3")
                    T.CommandString("KSv3", False)
                if rate == 4:
                    print("KSv4")
                    T.CommandString("KSv4", False)
             else:
                T.MoveAxis(P_axis, rate)
             

        elif direction == "right":
            T.MoveAxis(P_axis, -rate)  # Moves the telescope right
            if maestro_flag:
                print("KSpr")
                T.CommandString("KSpr", False)
                if rate == 0:
                    print("XXlr")
                    T.CommandString("XXlr", False)
                if rate == 1:
                    print("KSv1")
                    T.CommandString("KSv1", False)
                if rate == 2:
                    print("KSv2")
                    T.CommandString("KSv2", False)
                if rate == 3:
                    print("KSv3")
                    T.CommandString("KSv3", False)
                if rate == 4:
                    print("KSv4")
                    T.CommandString("KSv4", False)   
            else:
                T.MoveAxis(P_axis, rate)    

        else:
            print("Unknown button direction")
            return jsonify(status="error", message="Unknown direction")

        return jsonify(status="success", message=f"Received {direction} command")

    except Exception as e:
        print(f"Error during processing: {e}")
        return jsonify(status="error", message="Error during processing")

if __name__ == "__main__":

    # one time initialization here
    T = Telescope('localhost:32323', 0)  # Maestro IP at 192.168.1.140:11111
    print(f'Connected to {T.Name}')
    print(T.Description)
    T.Tracking = True   


    # launch the app
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)  # Disable reloader to avoid threading issues
