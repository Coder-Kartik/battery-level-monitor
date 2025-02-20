import psutil
import pandas as pd
import datetime

def log_battery_level():
    battery = psutil.sensors_battery()
    if battery is None:
        print("Battery information not available.")
        return

    level = battery.percent
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {"timestamp": timestamp, "battery_level": level}
    df = pd.DataFrame([data])

    # Append the data to the CSV file
    df.to_csv("battery_log.csv", mode="a", header=False, index=False)

    # Print output for visibility
    print(f"[{timestamp}] Battery Level: {level}%")

if __name__ == "__main__":
    log_battery_level()
