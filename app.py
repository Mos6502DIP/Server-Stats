from flask import Flask
import psutil
import datetime
import json

app = Flask(__name__)

def get_uptime():
    try:
        with open('/proc/uptime', 'r') as f:
            uptime_seconds = float(f.readline().split()[0])

        timedelta = datetime.timedelta(seconds=uptime_seconds)

        time = str(timedelta)

        return time[:-7]

    except Exception as e:
        return "Uptime is not available - Exception: " + str(e)


def get_temp():
    try:
        # Fetching temperatures from sensors
        temps = psutil.sensors_temperatures()

        if not temps:
            print("No temperature sensors found!")
        else:
            # Getting the first temperature reading
            for name, entries in temps.items():
                if entries:  # Check if entries list is not empty
                    main_temp = entries[0].current  # First temperature entry
                    return f"{main_temp}"

    except:
        return "Temperature Unknown"




@app.route('/stats')
def stats():
    uptime = get_uptime()
    temp = get_temp()
    cpu_usage = psutil.cpu_percent()

    return json.dumps({"uptime": uptime, "temp": temp, "cpu_usage": cpu_usage})


if __name__ == '__main__':
    app.run(host="0.0.0.0")
