import pandas as pd
import datetime
import psutil
import os

def log_battery_level():
    battery = psutil.sensors_battery()
    if battery is None:
        return
    
    level = battery.percent
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = {"timestamp": timestamp, "battery_level": level}
    df = pd.DataFrame([data])

    # Check if file exists to add headers only the first time
    file_exists = os.path.isfile("battery_log.csv")
    df.to_csv("battery_log.csv", mode="a", header=not file_exists, index=False)

if __name__ == "__main__":
    log_battery_level()
